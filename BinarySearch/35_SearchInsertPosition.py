#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    # Pythonic way.
    def searchInsert(self, nums, target):
        return len([x for x in nums if x < target])


class Solution_2(object):
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            if target == nums[mid]:
                return mid

            elif target > nums[mid]:
                left = mid + 1

            else:
                right = mid - 1

        return left

"""
[1,3,5,6]
5
[1,3,5,6]
2
[1,3,5,6]
7
[1,3,5,6]
0
"""
