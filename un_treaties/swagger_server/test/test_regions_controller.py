# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.region import Region  # noqa: E501
from swagger_server.test import BaseTestCase


class TestRegionsController(BaseTestCase):
    """RegionsController integration test stubs"""

    def test_get_regions(self):
        """Test case for get_regions

        Get the whole list of regions
        """
        response = self.client.open(
            '/api/regions',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
