#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


class Solution(object):
    # Binary Search, Yes!!
    def hIndex(self, citations):
        length = len(citations)
        left = 0
        right = length - 1
        while left <= right:
            # Disapproval / operator here(more slower), can use // or >> 1
            # mid = (left + right) / 2
            mid = (left + right) >> 1
            if citations[mid] == length - mid:
                return citations[mid]
            elif citations[mid] > length - mid:
                right = mid - 1
            else:
                left = mid + 1
        return length - (right + 1)


"""
[]
[0]
[23]
[0,1]
[1,1,1,1]
[4,4,4,4]
[0,1,4,5,6]
"""
