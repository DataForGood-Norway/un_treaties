# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.treaty import Treaty  # noqa: E501
from swagger_server.test import BaseTestCase


class TestTreatiesController(BaseTestCase):
    """TreatiesController integration test stubs"""

    def test_find_treaties_by_status(self):
        """Test case for find_treaties_by_status

        Finds treaties by status
        """
        query_string = [('status', 'available')]
        response = self.client.open(
            '/api/treaties/findByStatus',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_treaties_by_tags(self):
        """Test case for find_treaties_by_tags

        Finds treaties by tags
        """
        query_string = [('tags', 'tags_example')]
        response = self.client.open(
            '/api/treaties/findByTags',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_treaties(self):
        """Test case for get_treaties

        Get the list of treaties
        """
        response = self.client.open(
            '/api/treaties',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_treaty_by_id(self):
        """Test case for get_treaty_by_id

        Find a treaty by Id
        """
        response = self.client.open(
            '/api/treaties/{treatyId}'.format(treatyId=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
