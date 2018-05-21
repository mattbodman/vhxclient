#!/usr/bin/env python2
from errors import NoIdError
from datetime import datetime


class Collection(object):

    def __init__(self, client, _id=None):
        self._client = client
        self.id = _id
        self.type = None
        self.name = None
        if self.id:
            self.load()

    def load(self):
        if not self.id:
            raise NoIdError
        response = self._client.request('/collections/%s' % self.id, 'GET')
        for k in response.keys():
            setattr(self, k, response[k])

    def save(self):
        if not self.type:
            raise Exception('"type" must be one of "section", "category", "series", "season", "movie", or "playlist"')
        if not self.name:
            raise Exception('"name" is required')
        if type == 'season':
            if not self.season_number or not self.series_id:
                raise Exception('"season" collections require "season_number" and the "series_id" of the collection to'
                                'be added to')
        omitted_attributes = ['_client', '_embedded', '_links']
        data = {k: v for k, v in self.__dict__.items() if k not in omitted_attributes}
        for k, v in data.items():
            if isinstance(v, datetime):
                data[k] = v.isoformat()
        if not self.id:
            response = self._client.request('/collections', 'POST', data)
        else:
            response = self._client.request('/collections/%s' % self.id, 'PUT', data)
        for k in response.keys():
            setattr(self, k, response[k])

    def json(self):
        return {k: v for k, v in self.__dict__.items() if not k.startswith('_') and k not in ['json']}
