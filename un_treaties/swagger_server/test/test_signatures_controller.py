# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.signature import Signature  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSignaturesController(BaseTestCase):
    """SignaturesController integration test stubs"""

    def test_get_signatures_by_participant_id(self):
        """Test case for get_signatures_by_participant_id

        Find signatures for a given participant
        """
        response = self.client.open(
            '/api/signatures/participantId/{participantId}'.format(participantId=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_signatures_by_treaty_id(self):
        """Test case for get_signatures_by_treaty_id

        Find signatures for a given treaty
        """
        response = self.client.open(
            '/api/signatures/treatyId/{treatyId}'.format(treatyId=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
