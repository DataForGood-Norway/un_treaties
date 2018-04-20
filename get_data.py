import itertools
import re
import sys

import bs4
import pandas as pd
import requests

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


def make_df(url):
    """Make a data frame from a treaty URL."""
    print(url)
    treaty_soup = get_soup(url)

    # Parse the table of countries
    def resp_table_div(tag):
        return (tag.name == 'div' and
                'table-responsive' in tag.get('class', ''))
    tables = [str(t) for t in treaty_soup.find_all(resp_table_div)]
    for table in tables:
        try:
            df = pd.read_html(table, header=[0] if 'thead' in table else None)[0]
        except ValueError:  # Not a table after all
            continue
        if 'Participant' in df.columns:
            break
    else:
        print('Found no Participant-table!')

    # Get stuff from the top of the page
    fields = dict(
        Treaty='treatyCenter',
        Chapter='tcTextCenter',
        Date='treatyCenterSub',
        )
    for field, class_ in fields.items():
        field_text = treaty_soup.find(class_=class_).text.strip()
        df[field] = field_text.split('\n')[-1].strip()

    # Get notes from bottom table
    #   TODO

    # Try to convert date fields
    date_fields = ['ratification', 'accession', 'signature']
    for field in df.columns:
        if isinstance(field, int):
            continue
        if any([f in field.lower() for f in date_fields]):
            df[field] = _convert_date(df[field])

    # Other useful stuff
    df['URL'] = url

    return df


def _convert_date(data_s):
    re_date = re.compile('(\d\d? (jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec) \d{4})',
                         flags=re.IGNORECASE)
    data_l = list()
    for _, row in data_s.iteritems():
        match = re_date.search(str(row))
        data_l.append(match.group() if match else 'nan')

    return pd.to_datetime(pd.Series(data_l))

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
            except ValueError:   # Page without table
                continue


if __name__ == '__main__':
    try:
        url = sys.argv[1]
        df = make_df(url)
        import IPython; IPython.embed()
    except IndexError:
        for df in iter_treaties():  # itertools.islice(iter_treaties(), 5):
            print(df.head())
