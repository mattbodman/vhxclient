#!/usr/bin/env python2
import base64
import httplib2
import json
from errors import NotFoundError, InternalServerError, NotAcceptableError, PaymentRequiredError, BadRequestError, \
    UnauthorizedError


class VHXClient(object):

    def __init__(self, api_key, site_id=None):
        self.site_id = site_id
        if not api_key.endswith(':'):
            api_key += ':'
        encoded_key = base64.b64encode(api_key)
        self._headers = {
            'Authorization': 'Basic %s' % encoded_key,
            'Content-Type': 'application/json',
            'Cache-Control': 'no-cache'
        }
        try:
            # self._get('videos')
            pass
        except Exception:
            raise

    _http_client = httplib2.Http()

    _base_uri = 'https://api.vhx.tv'

    def request(self, uri='', method='', data=''):
        print uri
        try:
            response, body = self._http_client.request('%s/%s' % (self._base_uri, uri),
                                                       method, json.dumps(data), headers=self._headers)
            status = response.status
            if status in [200, 201, 304]:
                return json.loads(body)
            elif status == 401:
                raise UnauthorizedError
            elif status == 400:
                raise BadRequestError
            elif status == 402:
                raise PaymentRequiredError
            elif status == 404:
                raise NotFoundError
            elif status == 406:
                raise NotAcceptableError
            elif status >= 500:
                raise InternalServerError
        except Exception:
            raise

    def list(self, item, query='', sort=''):
        if item == 'collections' and sort and sort not in ['alphabetical', 'newest', 'oldest', 'latest']:
            raise Exception('"sort" must be on of "alphabetical", "newest", "oldest", or "latest"')
        if item == 'videos' and sort and sort not in ['alphabetical', 'newest', 'oldest', 'plays', 'finishes',
                                                      'duration']:
            raise Exception('"sort" must be on of "alphabetical", "newest", "oldest", "plays", "finishes"'
                            ' or "duration"')

        response = self.request('/%s?query=%s' % (item, query), 'GET')
        return response
