import bs4
import requests
import pandas

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

def make_df(url, name):
    """Make a data frame from a treaty URL."""
    print(url, name)
    treaty = get_soup(url)
    def resp_table_div(tag):
        return (tag.name == 'div' and
                'table-responsive' in tag.get('class', ''))
    df = pandas.read_html(str(treaty.find(resp_table_div)),
                          header=[0],
                          parse_dates=[1])[0]
    df['Treaty'] = name
    df['URL'] = url
    return df

def process(df):
    pass

def iter_treaties():
    base = get_soup(BASE + START_PAGE)
    for chapter_link in base(links_containing('Treaties.aspx')):
        chapter_soup = get_soup(BASE + chapter_link['href'])
        treaty_links = chapter_soup(links_containing('Details.aspx'))
        for link in treaty_links:
            name = link.text
            treaty_url = BASE + link['href']
            try:
                yield make_df(treaty_url, name)
            except:
                continue

if __name__ == '__main__':
    import itertools
    for df in itertools.islice(iter_treaties(), 5):
        print(df.head())
            
