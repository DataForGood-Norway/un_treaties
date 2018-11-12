import connexion
import six

from swagger_server.models.ratification import Ratification  # noqa: E501
from swagger_server import util


def get_ratifications_by_participant_id(participantId):  # noqa: E501
    """Find ratifications for a given participant

    Returns a list of ratifications signed for by a given participants. # noqa: E501

    :param participantId: Id of participant to return ratifications from.
    :type participantId: int

    :rtype: List[Ratification]
    """
    return 'do some magic!'


def get_ratifications_by_treaty_id(treatyId):  # noqa: E501
    """Find ratifications for a given treaty

    Returns a list of ratifications signed for a given treaty. # noqa: E501

    :param treatyId: Id of treaty to return ratifications from.
    :type treatyId: int

    :rtype: List[Ratification]
    """
    return 'do some magic!'
