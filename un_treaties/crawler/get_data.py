import pathlib
import re
import sys

import bs4
import pandas as pd
import requests

import un_treaties
from un_treaties.crawler import countries

BASE = 'https://treaties.un.org/Pages/'
START_PAGE = 'ParticipationStatus.aspx?clang=_en'


def get_soup(url, cache=False):
    """Read html from url or cache"""
    file_name = url.split("/")[-1]
    file_path = un_treaties.get_local_path(file_name)

    # Try to read from cache
    if cache:
        if file_path.exists():
            text = file_path.read_text()
        else:
            return get_soup(url, cache=False)

    # Download from URL and save to cache
    else:
        text = requests.get(url).text
        file_path.write_text(text)

    return bs4.BeautifulSoup(text, 'lxml')


def get_soup_from_file(path):
    text = pathlib.Path(path).read_text()
    return bs4.BeautifulSoup(text, 'lxml')


def links_containing(text):
    def filter(tag):
        return (tag.name == 'a' and
                text in tag.get('href', ''))
    return filter


def read_header_treaty(treaty_soup):
    """Read the treaty information before the tables
    containing the ratifications of the countries"""
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
            headerInfos[field] = re.sub( '\s+', ' ', field_text.text).strip()
    return headerInfos


def make_df(treaty_soup, url):
    """Make a data frame from a treaty URL."""

    # Parse the table of countries
    def resp_table_div(tag):
        return (tag.name == 'div' and
                'table-responsive' in tag.get('class', ''))
    tables = [str(t) for t in treaty_soup.find_all(resp_table_div)]
    for idx, table in enumerate(tables):
        # print('table #{}'.format(idx))
        try:
            df = pd.read_html(table, header=[0] if 'thead' in table else None)[0]
            # print(df.columns)
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
        print(f'WARN Found no Participant-table at {url}')
        return None, url

    # Some Participant-only tables get interpreted weirdly by pandas
    # Ex: https://treaties.un.org/Pages/ViewDetails.aspx?src=TREATY&mtdsg_no=I-4&chapter=1&clang=_en
    if all(df.Participant.isnull()):
        countries_list = df.columns.tolist()
        countries_list = countries_list[countries_list.index('Participant') + 1:]
        df = pd.DataFrame(dict(Participant=countries_list))

    # Normalize country names
    df.Participant = _normalize_country_names(df.Participant)

    # Get stuff from the top of the page
    for field, value in read_header_treaty(treaty_soup).items():
        # print(field, value)
        df[field] = value

    # Split PlaceAndDate
    df['TreatyPlace'], _, df['TreatyDate'] = zip(*[[x.strip() for x in d.partition(',')] for _, d in df['TreatyPlaceAndDate'].iteritems()])

    # Get notes from bottom table
    #   TODO

    # Try to convert date fields
    for field in df.columns:
        if isinstance(field, int):
            continue
        if field.startswith("Signature"):
            df["Signature"], _ = _convert_date(df[field])
            del df[field]
            continue
        mapper = _convert_field(field)
        if mapper:
            df['ActionDate'], action_type = _convert_date(df[field])
            df['ActionType'] = action_type.map(mapper).str.title()
            del df[field]

    return df, url


def _convert_field(data_s):
    re_field = re.compile('(ratification|acceptance|accession|succession|definitive signature|application|adoption|registration date|notification)[^,()]*(?:\((\w+)\))?',
                          flags=re.IGNORECASE)
    match = re_field.findall(data_s)
    if match:
        return dict(reversed(m) for m in match)
    else:
        return None


def _convert_date(data_s):
    re_date = re.compile('(\d\d? (jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)\w* \d{4}) *(\w*)',
                         flags=re.IGNORECASE)
    date_list, type_list = list(), list()
    for _, row in data_s.iteritems():
        match = re_date.search(str(row))
        date_list.append(match.groups()[0] if match else 'nan')
        type_list.append(match.groups()[-1] if match else '')

    return pd.to_datetime(pd.Series(date_list)), pd.Series(type_list)


def _normalize_country_names(country_list):
    return pd.Series([countries.normalize(c) for c in country_list])


def iter_treaties(cache=False):
    base_soup = get_soup(BASE + START_PAGE, cache=cache)
    for chapter_link in base_soup(links_containing('Treaties.aspx')):
        chapter_soup = get_soup(BASE + chapter_link['href'], cache=cache)
        treaty_links = chapter_soup(links_containing('Details.aspx'))
        for link in treaty_links:
            treaty_url = BASE + link['href']
            treaty_soup = get_soup(treaty_url, cache=cache)
            try:
                yield make_df(treaty_soup, url=treaty_url)
            except KeyError as e:   # Page without table
                print(e)
                continue


def main():
    use_cache = "--no-cache" not in sys.argv

    df_list = list()
    for i, (df, url) in enumerate(iter_treaties(use_cache)):
        if df is not None:
            print(f"{i:>3} {url}")
            df_list.append(df)

    df = pd.concat(df_list, sort=True)
    with un_treaties.resources.path("un_treaties.data", "un_treaties.csv") as csv_path:
        df.to_csv(csv_path)

    with un_treaties.resources.path("un_treaties.data", "un_treaties.json") as json_path:
        df.to_json(orient='records', path_or_buf=json_path)


if __name__ == '__main__':
    main()
