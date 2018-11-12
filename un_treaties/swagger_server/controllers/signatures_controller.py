import connexion
import six

from swagger_server.models.signature import Signature  # noqa: E501
from swagger_server import util


def get_signatures_by_participant_id(participantId):  # noqa: E501
    """Find signatures for a given participant

    Returns a list of signatures signed for by a given participants. # noqa: E501

    :param participantId: Id of participant to return signatures from.
    :type participantId: int

    :rtype: List[Signature]
    """
    return 'do some magic!'


def get_signatures_by_treaty_id(treatyId):  # noqa: E501
    """Find signatures for a given treaty

    Returns a list of signatures signed for a given treaty. # noqa: E501

    :param treatyId: Id of treaty to return signatures from.
    :type treatyId: int

    :rtype: List[Signature]
    """
    return 'do some magic!'
