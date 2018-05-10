#!/usr/bin/env python2

import base64
import httplib2
import json
from errors import NotFoundError, InternalServerError, NotAcceptableError, PaymentRequiredError, BadRequestError, \
    UnauthorizedError
from resource import Resource


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
            self._get('videos')
        except Exception:
            raise
        for resource in [
            'products',
            'customers',
            'watchlist',
            'videos',
            'collections',
            'authorizations',
            'analytics'
        ]:
            setattr(self, resource, Resource(self, resource))

    _http_client = httplib2.Http()

    _base_uri = 'https://api.vhx.tv'

    def _request(self, uri='', data='', item_id='', method=''):
        if self.site_id:
            print 'SITE ID', self.site_id
            if isinstance(data, str):
                data = {'site_id': self.site_id}
            elif isinstance(data, dict):
                data['site_id'] = self.site_id
        try:
            print data
            response, body = self._http_client.request('%s/%s/%s' % (self._base_uri, uri, item_id), method,
                                                       json.dumps(data), headers=self._headers)
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

    def _get(self, uri='', data='', item_id=''):
        return self._request(uri=uri, item_id=item_id, data=data, method='GET')

    def _post(self, uri='', data=''):
        return self._request(uri=uri, data=data, method='POST')

    def _put(self, uri='', item_id='', data=''):
        return self._request(uri=uri, item_id=item_id, data=data, method='PUT')
