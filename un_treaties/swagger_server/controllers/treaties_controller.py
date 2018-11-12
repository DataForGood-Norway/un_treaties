import connexion
import six

from swagger_server.models.treaty import Treaty  # noqa: E501
from swagger_server import util


def find_treaties_by_status(status):  # noqa: E501
    """Finds treaties by status

    Multiple status values can be provided with comma separated strings # noqa: E501

    :param status: Status values that need to be considered for filter
    :type status: List[str]

    :rtype: List[Treaty]
    """
    return 'do some magic!'


def find_treaties_by_tags(tags):  # noqa: E501
    """Finds treaties by tags

    Muliple tags can be provided with comma separated strings. Use tag1, tag2, tag3 for testing. # noqa: E501

    :param tags: Tags to filter by
    :type tags: List[str]

    :rtype: List[Treaty]
    """
    return 'do some magic!'


def get_treaties():  # noqa: E501
    """Get the list of treaties

    Treaties are returned as an object by name and some properties. # noqa: E501


    :rtype: List[Treaty]
    """
    return 'do some magic!'


def get_treaty_by_id(treatyId):  # noqa: E501
    """Find a treaty by Id

    Returns a single treaty # noqa: E501

    :param treatyId: Id of treaty to return
    :type treatyId: int

    :rtype: Treaty
    """
    return 'do some magic!'
