#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


class Solution(object):
    """
    Recursive way: easy to understand.  The key idea for this solution is:
    each operator in this string could be the last operator to be operated.
    We just iterator over all these cases.
    """

    def diffWaysToCompute(self, input):
        if input.isdigit():
            return [int(input)]

        res = []
        for i in xrange(len(input)):
            if input[i] in "+-*":
                res_left = self.diffWaysToCompute(input[:i])
                res_right = self.diffWaysToCompute(input[i + 1:])
                for left in res_left:
                    for right in res_right:
                        res.append(self.computer(left, right, input[i]))
        return res

    def computer(self, m, n, op):
        if op == "+":
            return m + n
        elif op == "-":
            return m - n
        else:
            return m * n


class Solution_2(object):
    # Use cache to avoid repeating subquestions in recursive way.
    def diffWaysToCompute(self, input):
        self.cache = {}
        return self.computerWithCache(input)

    def computerWithCache(self, input):
        if input.isdigit():
            self.cache[input] = [int(input)]
            return [int(input)]

        res = []
        for i in xrange(len(input)):
            if input[i] in "+-*":
                left_str = input[:i]
                res_left = (self.cache[left_str] if left_str in self.cache
                            else self.computerWithCache(input[:i]))
                right_str = input[i + 1:]
                res_right = (self.cache[right_str] if right_str in self.cache
                             else self.computerWithCache(input[i + 1:]))

                for left in res_left:
                    for right in res_right:
                        res.append(self.computer(left, right, input[i]))
        self.cache[input] = res
        return res

    def computer(self, m, n, op):
        if op == "+":
            return m + n
        elif op == "-":
            return m - n
        else:
            return m * n

"""
"0"
"2-1-1"
"2*3-4*5"
"3-6*7+8-12*1"
"""
