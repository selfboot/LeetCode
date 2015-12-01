#! /usr/bin/env python
# -*- coding: utf-8 -*-
import collections


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        # An OrderedDict is a dictionary subclass
        # that remembers the order in which its contents are added.
        self.cache = collections.OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1
        value = self.cache.pop(key)
        self.cache[key] = value
        return value

    def set(self, key, value):
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) == self.capacity:
            self.cache.popitem(last=False)
        else:
            pass
        self.cache[key] = value

"""
if __name__ == '__main__':
    ca = LRUCache(2)
    ca.set(2, 1)
    print "AA", ca.get(2)
    ca.set(2, 2)
    print "BB",  ca.get(2)
    ca.set(3, 3)
    print "CC", ca.get(3)
    # what if: print "CC", ca.get(2)
    ca.set(4, 1)
    print "CC", ca.get(2)
"""
