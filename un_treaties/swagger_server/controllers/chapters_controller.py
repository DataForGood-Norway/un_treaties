import connexion
import six

from swagger_server.models.chapter import Chapter  # noqa: E501
from swagger_server import util


def find_chapters_by_tags(tags):  # noqa: E501
    """Finds chapters by tags

    Muliple tags can be provided with comma separated strings. Use tag1, tag2, tag3 for testing. # noqa: E501

    :param tags: Tags to filter by
    :type tags: List[str]

    :rtype: List[Chapter]
    """
    return 'do some magic!'


def get_chapter_by_id(chapterId):  # noqa: E501
    """Find a chapter by Id

    Returns a single chapter # noqa: E501

    :param chapterId: Id of chapter to return
    :type chapterId: int

    :rtype: Chapter
    """
    return 'do some magic!'


def get_chapters():  # noqa: E501
    """Get the list of chapters

    Chapters are returned as an object by name and some properties. # noqa: E501


    :rtype: Chapter
    """
    return 'do some magic!'
