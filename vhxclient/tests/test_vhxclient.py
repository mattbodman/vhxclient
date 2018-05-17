#!/usr/bin/env python2
from vhxclient.video import Video

import unittest
from vhxclient import VHXClient
from vhxclient.errors import UnauthorizedError
import os

TEST_KEY = os.environ.get('VHX_TEST_API_KEY')
TEST_ID = os.environ.get('VHX_SITE_ID')


class TestMethods(unittest.TestCase):

    def setUp(self):
        self.vhx = VHXClient(TEST_KEY, TEST_ID)

    def test_connection(self):
        self.assertTrue(self.vhx.__class__.__name__ == 'VHXClient')

    def test_connection_error(self):
        vhx = VHXClient('bogus_api_key')
        self.assertRaises(UnauthorizedError, Video, vhx, 'foobar')

    def test_list_no_item(self):
        self.assertRaises(Exception, self.vhx.list)

    def test_list(self):
        r = self.vhx.list('collections')
        self.assertTrue(r['count'])

    def test_list_with_query(self):
        r = self.vhx.list('videos', query='zzzzzzzzzzzz')
        self.assertEqual(r['count'], 0)

    def test_list_with_bogus_sort(self):
        self.assertRaises(Exception, self.vhx.list, 'videos', sort='sldkfj')
