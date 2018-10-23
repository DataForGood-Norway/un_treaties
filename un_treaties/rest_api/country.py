from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# Data to serve with our API
COUNTRY = {
    "Norway": {
        "name": "Norway",
        "chapters_involved": [],
        "chapters_not_involved": [],
        "treaties_involved": [],
        "treaties_not_involved": [],
        "timestamp": get_timestamp(),
        "date_first_appearance": "",
        "text": "",
    },
    "Sweden": {
        "name": "Sweden",
        "chapters_involved": [],
        "chapters_not_involved": [],
        "treaties_involved": [],
        "treaties_not_involved": [],
        "timestamp": get_timestamp(),
        "date_first_appearance": "",
        "text": "",
    },
}

# Create a handler for our read (GET) COUNTRY
def read():
    """
    This function responds to a request for /api/COUNTRY
    with the complete lists of COUNTRY

    :return:        sorted list of COUNTRY
    """
    # Create the list of COUNTRY from our data
    return [COUNTRY[key] for key in sorted(COUNTRY.keys())]