from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# Data to serve with our API
CHAPTERS = {
    "1": {
        "number": 1,
        "title": "CHARTER OF THE UNITED NATIONS AND STATUTE OF THE INTERNATIONAL COURT OF JUSTICE",
        "uri": "https://treaties.un.org/pages/Treaties.aspx?id=1&subid=A&clang=_en",
        "treaties": [],
        "description": "",
    },
    "2": {
        "number": 2,
        "title": "PACIFIC SETTLEMENT OF INTERNATIONAL DISPUTES",
        "uri": "https://treaties.un.org/pages/Treaties.aspx?id=2&subid=A&clang=_en",
        "treaties": [],
        "description": "",
    },
}

# Create a handler for our read (GET) chapter
def read():
    """
    This function responds to a request for /api/chapter
    with the complete lists of chapters

    :return:        sorted list of chapters
    """
    # Create the list of chapters from our data
    return [CHAPTERS[key] for key in sorted(CHAPTERS.keys())]