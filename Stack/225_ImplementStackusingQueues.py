#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
from collections import deque


class Stack(object):
    def __init__(self):
        self._queue = deque()

    def push(self, x):
        # Pushing to back and
        # then rotating the queue until the new element is at the front
        q = self._queue
        q.append(x)
        for i in xrange(len(q) - 1):
            q.append(q.popleft())

    def pop(self):
        self._queue.popleft()

    def top(self):
        return self._queue[0]

    def empty(self):
        return not len(self._queue)

"""Test
if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    print s.top()
    s.pop()
    print s.empty()
    print s.top()
    s.pop()
    print s.empty()
"""
