#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


class Solution(object):
    # An easy approach which sorts the array first.
    def hIndex(self, citations):
        if not citations:
            return 0
        citations.sort()
        length = len(citations)
        for i in range(length, 0, -1):
            if citations[length-i] >= i:
                return i
        return 0


class Solution_2(object):
    # A faster approach use extra space.
    def hIndex(self, citations):
        length = len(citations)
        count = [0] * (length + 1)
        for i in citations:
            if i >= length:
                count[length] += 1
            else:
                count[i] += 1
        occur = 0
        # Dynamic programming here to
        # Sum the occuring times of citations bigger than one given value
        for i in range(length, 0, -1):
            occur += count[i]
            if occur >= i:
                return i
        return 0

"""
[]
[0]
[23]
[4,4,4,4]
[4, 0, 6, 1, 5]
"""
