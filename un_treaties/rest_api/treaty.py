from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# Data to serve with our API
TREATY = {
    "1": {
        "number_treaty": 1,
        "number_chapter": 1,
        "title": "Convention on the Prevention and Punishment of the Crime of Genocide",
        "timestamp": get_timestamp(),
        "date_entry_into_force": "",
        "date_registration": "",
        "participants": [],
        "text": "",
    },
    "2": {
        "number_treaty": 2,
        "number_chapter": 1,
        "title": "International Convention on the Elimination of All Forms of Racial Discrimination",
        "timestamp": get_timestamp(),
        "date_entry_into_force": "",
        "date_registration": "",
        "participants": [],
        "text": "",
    },
}

# Create a handler for our read (GET) TREATY
def read():
    """
    This function responds to a request for /api/TREATY
    with the complete lists of TREATY

    :return:        sorted list of TREATY
    """
    # Create the list of TREATY from our data
    return [TREATY[key] for key in sorted(TREATY.keys())]