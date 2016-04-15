#! /usr/bin/env python
# -*- coding: utf-8 -*-


class MinStack(object):
    # According to:
    # https://leetcode.com/discuss/45373/c-using-two-stacks-quite-short-and-easy-to-understand
    def __init__(self):
        self.stack_d = []
        self.stack_m = []

    def push(self, x):
        self.stack_d.append(x)
        if not self.stack_m or x <= self.getMin():
            self.stack_m.append(x)

    def pop(self):
        if self.top() == self.getMin():
            self.stack_m.pop()
        self.stack_d.pop()

    def top(self):
        return self.stack_d[-1]

    def getMin(self):
        return self.stack_m[-1]

'''
if __name__ == '__main__':
    one_stack = MinStack()
    one_stack.push(3)
    one_stack.push(4)
    one_stack.push(2)
    one_stack.push(1)

    print one_stack.getMin()
    one_stack.pop()
    print one_stack.getMin()
    one_stack.pop()
    print one_stack.getMin()
    one_stack.push(0)
    print one_stack.getMin()
'''
