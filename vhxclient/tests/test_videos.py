#!/usr/bin/env python2

import unittest
from vhxclient import VHXClient
import random
import string
from datetime import datetime
import os

TEST_KEY = os.environ.get('VHX_TEST_API_KEY')


class TestMethods(unittest.TestCase):

    def setUp(self):
        self.vhx = VHXClient(TEST_KEY)

    # all
    def test_list_videos(self):
        self.assertTrue(self.vhx.videos.all()['_embedded'])

    # retrieve
    def test_retrieve_video(self):
        video_id = self.vhx.videos.all()['_embedded']['videos'][0]['id']
        self.assertEqual(self.vhx.videos.retrieve(video_id)['id'], video_id)

    # create
    def test_create_video(self):
        time_available = datetime(2018, 1, 1).isoformat()
        time_unavailable = datetime(2018, 1, 31).isoformat()

        video = {
            'title': ''.join([random.choice(string.ascii_letters) for n in xrange(32)]),
            'description': 'A Test Video',
            'plans': ['free', 'public'],
            'time_available': time_available,
            'time_unavailable': time_unavailable,
            'metadata': {
                'rating': 'G',
                'language': 'EN',
                'country': 'AU',
                'cast': ['Jeff Goldblum', 'Ryan Gosling'],
                'release_year': 2000,
                'director': ['Wes Anderson'],
                'guests': ['Foo', 'Bar']
            }
        }
        new_video = self.vhx.videos.create(video)
        self.assertTrue(new_video['_links'])
        self.assertTrue(new_video['_embedded'])
        self.assertEqual(video['title'], new_video['title'])
        self.assertEqual(video['plans'], new_video['plans'])
        self.assertTrue(new_video['time_available'])
        self.assertTrue(new_video['time_unavailable'])
        self.assertEqual(video['metadata']['rating'], new_video['metadata']['rating'])
        self.assertEqual(video['metadata']['language'], new_video['metadata']['language'])
        self.assertEqual(video['metadata']['country'], new_video['metadata']['country'])
        self.assertEqual(video['metadata']['cast'], new_video['metadata']['cast'])
        self.assertEqual(video['metadata']['release_year'], new_video['metadata']['release_year'])
        self.assertEqual(video['metadata']['director'], new_video['metadata']['director'])
        self.assertEqual(video['metadata']['guests'], new_video['metadata']['guests'])  # undocumented custom field

    # update
    def test_update_video(self):
        # currently, 'geo_available', 'geo_unavailable' and 'short_description' can only be set by updating
        video = self.vhx.videos.all()['_embedded']['videos'][0]
        video['geo_available'] = 'AU,NZ'
        video['geo_unavailable'] = 'US'
        video['short_description'] = 'the short description'
        video['title'] = ''.join([random.choice(string.ascii_letters) for n in xrange(32)])
        self.vhx.videos.update(video['id'], video)
        updated_video = self.vhx.videos.retrieve(video['id'])
        self.assertEqual(video['title'], updated_video['title'])
        self.assertEqual(video['geo_available'], updated_video['geo_available'])
        self.assertEqual(video['geo_unavailable'], updated_video['geo_unavailable'])
        self.assertEqual(video['short_description'], updated_video['short_description'])
