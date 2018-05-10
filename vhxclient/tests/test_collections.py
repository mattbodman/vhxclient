#!/usr/bin/env python2

import unittest
from vhxclient import VHXClient
import random
import string
import os

TEST_KEY = os.environ.get('VHX_TEST_API_KEY')
TEST_ID = os.environ.get('VHX_SITE_ID')


class TestMethods(unittest.TestCase):

    def setUp(self):
        self.vhx = VHXClient(TEST_KEY, TEST_ID)

    # all
    def test_list_collections(self):
        print self.vhx.collections.all()['_embedded']['collections']
        self.assertTrue(self.vhx.collections.all()['_embedded'])

    # retrieve
    def test_retrieve_collection(self):
        collection_id = self.vhx.collections.all()['_embedded']['collections'][0]['id']
        self.assertEqual(self.vhx.collections.retrieve(collection_id)['id'], collection_id)

    # create
    def test_create_collection(self):
        collection = {
            'name': ''.join([random.choice(string.ascii_letters) for n in xrange(32)]),
            'type': 'series'
        }
        new_collection = self.vhx.collections.create(collection)
        self.assertTrue(new_collection['_links'])
        self.assertTrue(new_collection['_embedded'])
        self.assertEqual(new_collection['name'], new_collection['name'])

    # update
    def test_update_collection(self):
        collection = self.vhx.collections.all()['_embedded']['collections'][0]
        print collection
        collection_id = collection['id']
        collection_name = ''.join([random.choice(string.ascii_letters) for n in xrange(32)])
        collection = self.vhx.collections.update(collection_id, {'name': collection_name})
        #  collection = self.vhx.collections.retrieve(collection_id)
        new_collection_name = collection['name']
        self.assertEqual(collection_name, new_collection_name)
