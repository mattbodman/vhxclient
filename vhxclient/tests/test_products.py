#!/usr/bin/env python2

import unittest
from vhxclient import VHXClient
import os

TEST_KEY = os.environ.get('VHX_TEST_API_KEY')


class TestMethods(unittest.TestCase):

    def setUp(self):
        self.vhx = VHXClient(TEST_KEY)

    # all
    def test_list_products(self):
        self.assertTrue(self.vhx.products.all()['_embedded'])

    # retrieve
    def test_retrieve_products(self):
        products_id = self.vhx.products.all()['_embedded']['products'][0]['id']
        self.assertEqual(self.vhx.products.retrieve(products_id)['id'], products_id)
