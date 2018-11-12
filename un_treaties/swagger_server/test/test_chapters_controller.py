# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.chapter import Chapter  # noqa: E501
from swagger_server.test import BaseTestCase


class TestChaptersController(BaseTestCase):
    """ChaptersController integration test stubs"""

    def test_find_chapters_by_tags(self):
        """Test case for find_chapters_by_tags

        Finds chapters by tags
        """
        query_string = [('tags', 'tags_example')]
        response = self.client.open(
            '/api/chapters/findByTags',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_chapter_by_id(self):
        """Test case for get_chapter_by_id

        Find a chapter by Id
        """
        response = self.client.open(
            '/api/chapters/{chapterId}'.format(chapterId=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_chapters(self):
        """Test case for get_chapters

        Get the list of chapters
        """
        response = self.client.open(
            '/api/chapters',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
