#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution(object):
    # Attention: the latest version of your product fails the quality check
    # That's saying, given n versions must have at least one bad version.
    def firstBadVersion(self, n):
        if n <= 0:
            return 0
        left, right = 1, n
        while left < right:
            mid = (left + right) / 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return right
