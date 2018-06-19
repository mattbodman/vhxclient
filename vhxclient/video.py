#!/usr/bin/env python2
from errors import NoIdError
from datetime import datetime


class Video(object):

    def __init__(self, client, _id=None):
        self._client = client
        self.id = _id
        self.title = None
        if self.id:
            self.load()

    def load(self):
        if not self.id:
            raise NoIdError
        response = self._client.request('/videos/%s' % self.id, 'GET')
        for k in response.keys():
            setattr(self, k, response[k])

    def save(self):
        omitted_attributes = ['_client', '_embedded', '_links']
        data = {k: v for k, v in self.__dict__.items() if k not in omitted_attributes}
        for k, v in data.items():
            if isinstance(v, datetime):
                data[k] = v.isoformat()
        if not self.id:
            response = self._client.request('/videos', 'POST', data)
            print 'FROM POST', response
        else:
            response = self._client.request('/videos/%s' % self.id, 'PUT', data)
            print 'FROM PUT', response
        for k in response.keys():
            setattr(self, k, response[k])

    @property
    def json(self):
        omitted_attributes = ['_client', 'json']
        return {k: v for k, v in self.__dict__.items() if k not in omitted_attributes}
