from un_treaties import data


# Create a handler for our read (GET) TREATY
def read():
    """
    This function responds to a request for /api/TREATY
    with the complete lists of TREATY

    :return:        sorted list of TREATY
    """
    # Create the list of TREATY from our data
    return data.as_dict()
