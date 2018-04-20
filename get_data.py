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
    df = pd.read_html(str(treaty_soup.find_all(resp_table_div)), header=[0],
                      parse_dates=['Accession(a)','Date of Adoption'])[0]

    # Get stuff from the top of the page
    fields = dict(
        entryForce='ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolderInnerPage_rptEIF_ctl00_tcText',
        registration='ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolderInnerPage_rptRegistration_ctl00_tcText',
        status='ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolderInnerPage_rptStatus_ctl00_tcText',
        pdf='ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolderInnerPage_rptText_ctl00_tcText',
        Treaty='ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolderInnerPage_rptTreaty_ctl00_tcTreaty',
        Chapter='ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolderInnerPage_rptHead_ctl00_tcText',
        Date='ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolderInnerPage_rptTreaty_ctl00_tcText',
        )
    for field, id_ in fields.items():
        print(field)
        field_text = treaty_soup.find(id=id_)
        if field_text:
            df[field] = field_text.text.strip().split('\n')[-1].strip()

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
            try:
                yield process(make_df(treaty_url))
            except KeyError:   # Page without table
                continue
            #except ValueError:   # Page without table
            #    continue


if __name__ == '__main__':
    for df in iter_treaties():  # itertools.islice(iter_treaties(), 5):
        print(df.head())
