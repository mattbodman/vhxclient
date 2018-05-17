#!/usr/bin/env python2


class Resource(object):
    def __init__(self, parent, resource_type):
        self.resource_type = resource_type
        self.parent = parent

    def all(self):
        return self.parent._get(self.resource_type)

    def create(self, data):
        return self.parent._post(self.resource_type, data)

    def update(self, item_id, data):
        return self.parent._put(self.resource_type, item_id=item_id, data=data)

    def retrieve(self, item_id):
        return self.parent._get(self.resource_type, item_id=item_id)

    #  for adding items to collections
    def add(self, item_id, data):
        return self.parent._put(self.resource_type, item_id=item_id, data=data, additional='items')
