#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Refer to https://leetcode.com/discuss/857/constant-space-solution


class Solution(object):
    def singleNumber(self, nums):
        once = 0
        twice = 0
        third = 0
        for num in nums:
            twice |= once & num
            once ^= num
            third = once & twice
            once &= ~third
            twice &= ~third

        return once

"""
[1]
[1,1,1,2,2,2,3,4,4,4]
"""
