#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# @Last Modified time: 2016-08-29 10:15:24


class Solution(object):
    """ Heap merge is helpfull.
    """
    def kthSmallest(self, matrix, k):
        import heapq
        return list(heapq.merge(*matrix))[k - 1]


class Solution(object):
    """ Binary Search can solve this too.
    """
    def kthSmallest(self, matrix, k):


"""
[[1]]
1
[[1,2,3], [4,5,6], [7,8,9]]
3
[[ 1, 5, 9], [10, 11, 13], [12, 13, 15]]
8
"""
