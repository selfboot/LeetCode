#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


class Queue(object):
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        data_keep = []
        while self.data:
            val = self.data.pop()
            if self.data:
                data_keep.append(val)
        while data_keep:
            self.data.append(data_keep.pop())

    def peek(self):
        data_copy = self.data[:]
        val = data_copy.pop()
        while data_copy:
            val = data_copy.pop()
        return val

    def empty(self):
        return not self.data

if __name__ == '__main__':
    q = Queue()
    q.push(2)
    q.push(3)
    q.push(4)
    print q.peek()
    q.pop()
    print q.peek()
    q.pop()
    q.pop()
    print q.empty()
