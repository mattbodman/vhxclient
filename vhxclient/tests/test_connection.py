#!/usr/bin/env python2

import unittest
from vhxclient import VHXClient
from vhxclient.errors import UnauthorizedError
import os

TEST_KEY = os.environ.get('VHX_TEST_API_KEY')
TEST_ID = os.environ.get('VHX_SITE_ID')


class TestMethods(unittest.TestCase):

    def test_connection(self):
        vhx = VHXClient(TEST_KEY, TEST_ID)
        self.assertTrue(vhx.__class__.__name__ == 'VHXClient')

    def test_connection_error(self):
        self.assertRaises(UnauthorizedError, VHXClient, 'bogus_api_key')
