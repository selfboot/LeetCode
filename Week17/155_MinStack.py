#! /usr/bin/env python
# -*- coding: utf-8 -*-


class MinStack(object):
    def __init__(self):
        self.collection = []
        self.min_num = None

    def push(self, x):
        if not self.min_num:
            self.min_num = x
        if x < self.min_num:
            self.min_num = x
        self.collection.append(x)

    def pop(self):
        if self.collection:
            pop_num = self.collection.pop()
            # Update the min_num
            if pop_num == self.min_num:
                if self.collection:
                    self.min_num = self.collection[0]
                    for num in self.collection:
                        self.min_num = min(self.min_num, num)
                else:
                    self.min_num = None
            else:
                pass

    def top(self):
        if self.collection:
            return self.collection[-1]
        else:
            return None

    def getMin(self):
        return self.min_num

""" Test
if __name__ == '__main__':
    one_stack = MinStack()
    one_stack.push(2)
    one_stack.push(0)
    one_stack.push(3)
    one_stack.push(0)

    print one_stack.getMin()
    print one_stack.pop()
    print one_stack.getMin()
    print one_stack.pop()
    print one_stack.getMin()
    print one_stack.pop()
    print one_stack.getMin()
"""
