#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


class Queue(object):
    """
    Use python list as the underlying data structure for stack.
    Add a "move()" method to simplify code: it moves all elements
    of the "inStack" to the "outStack" when the "outStack" is empty.
    """
    def __init__(self):
        self.in_stack, self.out_stack = [], []

    def push(self, x):
        self.in_stack.append(x)

    def pop(self):
        self.move()
        self.out_stack.pop()

    def peek(self):
        self.move()
        return self.out_stack[-1]

    def empty(self):
        return (not self.in_stack) and (not self.out_stack)

    def move(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

'''
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
'''
