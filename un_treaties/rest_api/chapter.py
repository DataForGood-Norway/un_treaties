from datetime import datetime
from un_treaties import data


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# Create a handler for our read (GET) chapter
def read():
    """
    This function responds to a request for /api/chapter
    with the complete lists of chapters

    :return:        sorted list of chapters
    """
    df = data.as_dataframe()
    # Create the list of chapters from our data
    name_chapters = list(df['Chapter'].unique())
    # TODO Right now missing an entire chapter, chapter's number could be kept in the title when parsing
    return list(zip(range(1,len(name_chapters)+1), name_chapters))


def read_by_id(id):
    pass