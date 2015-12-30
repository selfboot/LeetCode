#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
from Queue import Queue


class Stack(object):
    def __init__(self):
        self.queue = Queue()

    def push(self, x):
        self.queue.put(x)

    def pop(self):
        q_keep = Queue()
        while not self.queue.empty():
            val = self.queue.get()
            if self.queue.empty():
                break
            else:
                q_keep.put(val)
        self.queue = q_keep

    def top(self):
        q_keep = Queue()
        while not self.queue.empty():
            val = self.queue.get()
            q_keep.put(val)
        self.queue = q_keep
        return val

    def empty(self):
        return self.queue.empty()

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
