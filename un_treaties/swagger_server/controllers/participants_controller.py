import connexion
import six

from swagger_server.models.participant import Participant  # noqa: E501
from swagger_server import util


def get_participant_by_id(participantId):  # noqa: E501
    """Find a participants by Id

    Returns a single participant # noqa: E501

    :param participantId: Id of participant to return
    :type participantId: int

    :rtype: Participant
    """
    return 'do some magic!'


def get_participant_by_name(name):  # noqa: E501
    """Get participant by participant&#39;s name

    Returns a single participants # noqa: E501

    :param name: The name of the participant that needs to be fetched.
    :type name: str

    :rtype: Participant
    """
    return 'do some magic!'


def get_participants():  # noqa: E501
    """Get the total list of participants

    Participants are returned as an object. (Present in the treaties, or not) # noqa: E501


    :rtype: Participant
    """
    return 'do some magic!'


def participants_regions():  # noqa: E501
    """Returns participants by world&#39;s regions

     # noqa: E501


    :rtype: object
    """
    return 'do some magic!'
