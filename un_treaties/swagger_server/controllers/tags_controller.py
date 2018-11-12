import connexion
import six

from swagger_server.models.tag import Tag  # noqa: E501
from swagger_server import util


def get_tags():  # noqa: E501
    """Get the whole list of tags

    Tags are returned as an object. # noqa: E501


    :rtype: Tag
    """
    return 'do some magic!'
