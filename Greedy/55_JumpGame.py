#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# @Last Modified time: 2016-06-27 12:58:19


class Solution(object):
    def canJump(self, nums):
        """
        The main idea is to see if current element can be
        reached by previous max jump.
        If not, return false. If true, renew the max jump.
        """
        length = len(nums)
        index, max_distance = 0, nums[0]

        while index < length:
            # Prune here.
            if max_distance >= length - 1:
                return True

            if max_distance >= index:
                max_distance = max(max_distance, index + nums[index])
            else:
                # Current position cannot be reached.
                return False
            index += 1

        return True

"""
[0]
[2,3,1,1,4]
[3,2,1,0,4]
[1,3,5,0,0,0,0,0]
"""
