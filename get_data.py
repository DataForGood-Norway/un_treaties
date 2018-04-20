import itertools

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
    df = pd.read_html(str(treaty_soup.find(resp_table_div)), header=[0],
                      parse_dates=[1])[0]

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

    # Other useful stuff
    df['URL'] = url

    return df


def process(df):
    return df



def iter_treaties():
    base_soup = get_soup(BASE + START_PAGE)
    for chapter_link in base_soup(links_containing('Treaties.aspx')):
        chapter_soup = get_soup(BASE + chapter_link['href'])
        treaty_links = chapter_soup(links_containing('Details.aspx'))
        for link in treaty_links:
            treaty_url = BASE + link['href']
            yield process(make_df(treaty_url))


if __name__ == '__main__':
    for df in iter_treaties():  # itertools.islice(iter_treaties(), 5):
        print(df.head())
