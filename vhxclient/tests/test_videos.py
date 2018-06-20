#!/usr/bin/env python2
import unittest
from vhxclient import VHXClient
import random
import string
from datetime import datetime
import os
from vhxclient.video import Video
from vhxclient.errors import NoIdError, NotFoundError


TEST_KEY = os.environ.get('VHX_TEST_API_KEY')
TEST_ID = os.environ.get('VHX_SITE_ID')


class TestMethods(unittest.TestCase):

    def setUp(self):
        self.vhx = VHXClient(TEST_KEY, TEST_ID)

    # no id error
    def test_load_video_no_id(self):
        v = Video(self.vhx)
        self.assertRaises(NoIdError, v.load)

    # not found
    def test_load_not_found_video(self):
        self.assertRaises(NotFoundError, Video, self.vhx, 'foobar_id')

    # load
    def test_load_video(self):

        attributes = ['_embedded', '_links', 'advertising', 'capabilities', 'created_at', 'description', 'drm',
                      'duration', 'finishes_count', 'geo_available', 'geo_unavailable', 'id', 'is_available',
                      'is_commenting_enabled', 'is_free', 'json', 'live_status', 'live_video', 'load', 'metadata',
                      'name', 'plans', 'plays_count', 'save', 'scheduled_at', 'short_description', 'status',
                      'thumbnail', 'time_available', 'time_unavailable', 'title', 'tracks', 'type', 'updated_at']
        v = Video(self.vhx, 277568)
        v.load()
        self.assertEqual(v.title, 'TEST VIDEO DO NOT DELETE')
        self.assertEqual(v.description, 'TEST LONG DESCRIPTION DO NOT EDIT')
        self.assertEqual([a for a in attributes if not a.startswith('_')], [a for a in dir(v) if not a.startswith('_')])

    # create
    def test_save_video_new(self):
        v = Video(self.vhx)
        title = ''.join([random.choice(string.ascii_letters) for n in xrange(32)])
        v.title = title
        v.description = 'A Test Description for %s' % v.title
        v.plans = ['free', 'public']
        v.time_available = datetime(2018, 1, 1)
        v.time_unavailable = datetime(2018, 1, 31)
        v.metadata = {
                'rating': 'G',
                'language': 'EN',
                'country': 'AU',
                'cast': ['Jeff Goldblum', 'Ryan Gosling'],
                'release_year': 2000,
                'director': ['Wes Anderson'],
                'guests': ['Foo', 'Bar']
            }
        v.save()
        self.assertTrue(v.id)
        self.assertEqual(v.title, title)

    # update
    def test_save_video_existing(self):
        short_description = ''.join([random.choice(string.ascii_letters) for n in xrange(32)])
        v = Video(self.vhx, 284037)
        v.short_description = short_description
        v.save()
        self.assertEqual(v.short_description, short_description)
