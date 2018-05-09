import itertools
import re
import sys

import bs4
import pandas as pd
import requests
import pycountry

BASE = 'https://treaties.un.org/Pages/'
START_PAGE = 'ParticipationStatus.aspx?clang=_en'


def get_soup(url):
    text = requests.get(url).text
    return bs4.BeautifulSoup(text, 'lxml')


def links_containing(text):
    def filter(tag):
        return (tag.name == 'a' and
                text in tag.get('href', ''))
    return filter


def read_header_treaty(url):
    """Read the treaty information before the tables 
    containing the ratifications of the countries"""
    treaty_soup = get_soup(url)
    headerInfos = {}
    fields = dict(
        entryForce='ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolderInnerPage_rptEIF_ctl00_tcText',
        registration='ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolderInnerPage_rptRegistration_ctl00_tcText',
        status='ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolderInnerPage_rptStatus_ctl00_tcText',
        pdf='ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolderInnerPage_rptText_ctl00_tcText',
        Treaty='ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolderInnerPage_rptTreaty_ctl00_tcTreaty',
        Chapter='ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolderInnerPage_rptHead_ctl00_tcText',
        TreatyPlaceAndDate='ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolderInnerPage_rptTreaty_ctl00_tcText',
        )
    for field, id_ in fields.items():
        field_text = treaty_soup.find(id=id_)
        if field_text:
            #print(field, ':\t', field_text) # Patrick debug             
            #print(field, ':\t', field_text.text.strip()) # Patrick debug 
            #print(field, ':\t', field_text.text.strip().split('\n')[-1].strip())
            headerInfos[field] = re.sub( '\s+', ' ', field_text.text).strip()
    return headerInfos
    
def make_df(url):
    """Make a data frame from a treaty URL."""
    print('parsed URL: ', url)
    treaty_soup = get_soup(url)

    # Parse the table of countries
    def resp_table_div(tag):
        return (tag.name == 'div' and
                'table-responsive' in tag.get('class', ''))
    tables = [str(t) for t in treaty_soup.find_all(resp_table_div)]
    for idx, table in enumerate(tables):
        print('table #{}'.format(idx))
        try:
            df = pd.read_html(table, header=[0] if 'thead' in table else None)[0]
            print(df.columns)
        except ValueError:  # Not a table after all
            continue
        if len(df) == 0:
            continue
        
        #import IPython; IPython.embed()
        participant_cols = [c for c in df.columns if str(c).lower().startswith('participant')]
        if participant_cols:
            if len(participant_cols) > 1:
                raise ValueError(f"Found more than one participant column: {participant_cols}")
            df.rename(columns={participant_cols[0]: "Participant"}, inplace=True)
        if 'Participant' in df.columns:
            break
            
    # if no break, do the 'else'
    else:
        print('table #{}: Found no Participant-table!'.format(idx))
        return

    
    # Some Participant-only tables get interpreted weirdly by pandas
    # Ex: https://treaties.un.org/Pages/ViewDetails.aspx?src=TREATY&mtdsg_no=I-4&chapter=1&clang=_en
    if all(df.Participant.isnull()):
        countries_list = df.columns.tolist()
        countries_list = countries_list[countries_list.index('Participant') + 1:]
        df = pd.DataFrame(dict(Participant=countries_list))

    # Normalize country names
    df.Participant = _normalize_country_names(df.Participant)

    # Get stuff from the top of the page
    for field, value in read_header_treaty(url).items():
        print(field, value)
        df[field] = value

    # Split PlaceAndDate
    df['TreatyPlace'], _, df['TreatyDate'] = zip(*[[x.strip() for x in d.partition(',')] for _, d in df['TreatyPlaceAndDate'].iteritems()])

    # Get notes from bottom table
    #   TODO



    # Try to convert date fields
    date_fields = ['ratification', 'accession', 'signature', 'succesion',
                   'application', 'adoption', 'registration date']
    for field in df.columns:
        if isinstance(field, int):
            continue
        is_date_field = [f for f in date_fields if f in field.lower()]
        if is_date_field:
            # df[field] = _convert_date(df[field])
            df['ActionDate'] = _convert_date(df[field])
            df['ActionType'] = is_date_field[0].title()

    # Other useful stuff
    df['URL'] = url

    return df


def _convert_date(data_s):
    re_date = re.compile('(\d\d? (jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)\w* \d{4})',
                         flags=re.IGNORECASE)
    data_l = list()
    for _, row in data_s.iteritems():
        match = re_date.search(str(row))
        data_l.append(match.group() if match else 'nan')

    return pd.to_datetime(pd.Series(data_l))


def _normalize_country_names(countries):
    pattern = re.compile(r'[,0-9)(\[\]]')   # Only keep letters and spaces
    normalized = list()

    for country in countries:
        try:
            country_name = pattern.sub('', country).strip()
        except TypeError:
            normalized.append('No country')
            continue

        try:
            codes = pycountry.countries.lookup(country_name)
            normalized.append(codes.alpha_3)
        except LookupError:
            # TODO: Do a second more manual search through pycountry
            normalized.append(country_name)

    return pd.Series(normalized)


def process(df):
    return df


def iter_treaties():
    base_soup = get_soup(BASE + START_PAGE)
    for chapter_link in base_soup(links_containing('Treaties.aspx')):
        chapter_soup = get_soup(BASE + chapter_link['href'])
        treaty_links = chapter_soup(links_containing('Details.aspx'))
        for link in treaty_links:
            treaty_url = BASE + link['href']
            try:
                yield process(make_df(treaty_url))
            except KeyError as e:   # Page without table
                print(e)
                continue
           #except ValueError:   # Page without table
            #    continue


if __name__ == '__main__':
    if len(sys.argv) > 1:
        url = sys.argv[1]
        df = make_df(url)
        import IPython; IPython.embed()
    else:
        #  df_list = [df for df in itertools.islice(iter_treaties(), 250) if df is not None]
        #  df_list = [df for df in iter_treaties() if df is not None]

        df_list = list()
        for i, df in enumerate(iter_treaties()):
            print(i)
            if df is not None:
                df_list.append(df)

            if not i % 10:
                print('Saving!')
                df = pd.concat(df_list)
                df.to_csv(f'un_treaties_{i:04d}.csv')

        df = pd.concat(df_list)
        df.to_csv('un_treaties.csv')
        import IPython; IPython.embed()
