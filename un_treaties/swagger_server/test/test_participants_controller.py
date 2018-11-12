# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.participant import Participant  # noqa: E501
from swagger_server.test import BaseTestCase


class TestParticipantsController(BaseTestCase):
    """ParticipantsController integration test stubs"""

    def test_get_participant_by_id(self):
        """Test case for get_participant_by_id

        Find a participants by Id
        """
        response = self.client.open(
            '/api/participants/{participantId}'.format(participantId=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_participant_by_name(self):
        """Test case for get_participant_by_name

        Get participant by participant's name
        """
        response = self.client.open(
            '/api/participants/name/{name}'.format(name='name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_participants(self):
        """Test case for get_participants

        Get the total list of participants
        """
        response = self.client.open(
            '/api/participants',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_participants_regions(self):
        """Test case for participants_regions

        Returns participants by world's regions
        """
        response = self.client.open(
            '/api/participants/regions',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
