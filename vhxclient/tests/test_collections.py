#!/usr/bin/env python2
import unittest
from vhxclient import VHXClient
import random
import string
from datetime import datetime
import os
from vhxclient.collection import Collection
from vhxclient.errors import NoIdError, NotFoundError

TEST_KEY = os.environ.get('VHX_TEST_API_KEY')
TEST_ID = os.environ.get('VHX_SITE_ID')


class TestMethods(unittest.TestCase):

    def setUp(self):
        self.vhx = VHXClient(TEST_KEY, TEST_ID)

    def test_load_collection_no_id(self):
        c = Collection(self.vhx)
        self.assertRaises(NoIdError, c.load)

    def test_load_not_found_collection(self):
        self.assertRaises(NotFoundError, Collection, self.vhx, 'foobar_id')

    def test_load_collection(self):

        attributes = ['_embedded', '_links', 'created_at', 'description', 'files_count', 'geo_available',
                      'geo_unavailable', 'has_free_videos', 'id', 'is_available', 'is_featured', 'items_count', 'json',
                      'load', 'metadata', 'name', 'plans', 'save', 'seasons_count', 'short_description', 'slug',
                      'thumbnail', 'type', 'updated_at']
        c = Collection(self.vhx, 54052)
        c.load()
        self.assertEqual(c.name, 'TEST COLLECTION DO NOT DELETE')
        self.assertEqual(c.description, 'TEST LONG DESCRIPTION DO NOT DELETE')
        self.assertEqual([a for a in attributes if not a.startswith('_')], [a for a in dir(c) if not a.startswith('_')])

    def test_save_collection_no_type(self):
        c = Collection(self.vhx)
        self.assertRaises(Exception, c.save)

    def test_save_collection_new(self):
        c = Collection(self.vhx)
        name = ''.join([random.choice(string.ascii_letters) for n in range(32)])
        c.name = name
        c.type = 'series'
        c.description = 'A Test Description for %s' % c.name
        c.plans = ['free', 'public']
        c.time_available = datetime(2018, 1, 1)
        c.time_unavailable = datetime(2018, 1, 31)
        c.metadata = {
                'rating': 'G',
                'language': 'EN',
                'country': 'AU',
                'cast': ['Jeff Goldblum', 'Ryan Gosling'],
                'release_year': 2000,
                'director': ['Wes Anderson'],
                'guests': ['Foo', 'Bar']
            }
        c.save()
        self.assertTrue(c.id)
        self.assertEqual(c.name, name)

    def test_save_collection_existing(self):
        short_description = ''.join([random.choice(string.ascii_letters) for n in xrange(32)])
        c = Collection(self.vhx, 54052)
        c.thumbnail_url = 'https://image.tmdb.org/t/p//original//yatxjpSxWREk1SwAivvc5hlEZqJ.jpg'
        c.short_description = short_description
        c.save()
        self.assertEqual(c.short_description, short_description)

    def test_save_new_season(self):
        c = Collection(self.vhx)
        c.type = 'season'
        c.name = 'A TEST SEASON'
        c.thumbnail_url = 'https://image.tmdb.org/t/p//original//egPM9Lrlm6h2wHRpJkyRux2psqi.jpg'
        c.season_number = 1
        c.series_id = 54052
        c.save()
        self.assertTrue(c.id)
