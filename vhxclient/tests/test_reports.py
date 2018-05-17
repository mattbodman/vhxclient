#!/usr/bin/env python2
import unittest
from vhxclient import VHXClient
from datetime import datetime
import os
from vhxclient.errors import InvalidReportTypeError, NoIdError
from vhxclient.report import Report

TEST_KEY = os.environ.get('VHX_TEST_API_KEY')
TEST_ID = os.environ.get('VHX_SITE_ID')


class TestMethods(unittest.TestCase):

    def setUp(self):
        self.vhx = VHXClient(TEST_KEY, TEST_ID)

    def test_valid_type(self):
        self.assertRaises(InvalidReportTypeError, Report, self.vhx)

    def test_get_traffic_report(self):
        r = Report(self.vhx, 'traffic')
        self.assertTrue(r.data)

    def test_get_report_by_month_missing_from_or_to_date(self):
        self.assertRaises(InvalidReportTypeError, Report, self.vhx, 'traffic', by='month')

    def test_get_report_by_month(self):
        r = Report(self.vhx, 'units', by='month', from_date=datetime(2018, 1, 1), to_date=datetime(2018, 1, 31))
        self.assertTrue(1, 2)

    def test_get_units_report(self):
        r = Report(self.vhx, 'units')
        self.assertTrue(r.data)

    def test_get_income_statement_report(self):
        r = Report(self.vhx, 'income_statement')
        self.assertTrue(r.data)

    def test_get_subscribers_report(self):
        r = Report(self.vhx, 'subscribers')
        self.assertTrue(r.data)

    def test_get_churn_report(self):
        r = Report(self.vhx, 'churn')
        self.assertTrue(r.data)

    def test_get_video__report_no_id(self):
        self.assertRaises(NoIdError, Report, self.vhx, 'video')

    def test_get_video_platforms_report(self):
        r = Report(self.vhx, 'video.platforms', 277568)
        self.assertIsInstance(r.data, list)

    def test_get_video_geography_report(self):
        r = Report(self.vhx, 'video.geography', 277568)
        self.assertIsInstance(r.data, list)

    def test_get_video_subtitles_report(self):
        r = Report(self.vhx, 'video.subtitles', 277568)
        self.assertIsInstance(r.data, list)
