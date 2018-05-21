#!/usr/bin/env python2
from errors import InvalidReportTypeError, NoIdError


class Report(object):

    def __init__(self, client, report_type=None, video_id=None, by=None, from_date=None, to_date=None):
        allowed_report_types = ['traffic', 'income_statement', 'units', 'subscribers', 'churn', 'video',
                                'video.platforms', 'video.geography', 'video.subtitles']
        if report_type not in allowed_report_types:
            raise InvalidReportTypeError('Allowed report types are %s' % allowed_report_types)
        if report_type in ['video', 'video.platforms', 'video.geography', 'video.subtitles'] and not video_id:
            raise NoIdError('This report requires a video id')
        if by and (not from_date or not to_date):
            raise InvalidReportTypeError('"by", "from_date" and "to_date" are required together')
        if from_date:
            from_date = from_date.strftime('%Y-%m-%d')
        if to_date:
            to_date = to_date.strftime('%Y-%m-%d')
        self.type = report_type
        self._client = client
        if by:
            response = self._client.request(
                '/analytics?type=%s&video_id=%s&by=%s&from=%s&to=%s' % (
                    self.type, video_id, by, from_date, to_date), 'GET')
        else:
            response = self._client.request('/analytics?type=%s&video_id=%s' % (self.type, video_id), 'GET')
        for k in response.keys():
            setattr(self, k, response[k])

    def json(self):
        return {k: v for k, v in self.__dict__.items() if not k.startswith('_')}
