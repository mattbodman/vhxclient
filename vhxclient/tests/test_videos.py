#!/usr/bin/env python2

import unittest
from vhxclient import VHXClient
import random
import string
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
        video = {
            'title': ''.join([random.choice(string.ascii_letters) for n in xrange(32)]),
            'description': 'A Test Video'
        }
        new_video = self.vhx.videos.create(video)
        self.assertTrue(new_video['_links'])
        self.assertTrue(new_video['_embedded'])
        self.assertEqual(video['title'], new_video['title'])

    # update
    def test_update_video(self):
        video = self.vhx.videos.all()['_embedded']['videos'][0]
        video_id = video['id']
        video_title = ''.join([random.choice(string.ascii_letters) for n in xrange(32)])
        self.vhx.videos.update(video_id, {'title': video_title})
        video = self.vhx.videos.retrieve(video_id)
        new_video_title = video['title']
        self.assertEqual(video_title, new_video_title)
