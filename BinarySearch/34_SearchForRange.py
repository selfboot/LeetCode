#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    # log(n) here.
    def firstAppear(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            if target == nums[mid] and mid - 1 >= left and target == nums[mid - 1]:
                right = mid - 1
            elif target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    # log(n) again.
    def lastAppear(set, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            if target == nums[mid] and mid + 1 <= right and target == nums[mid + 1]:
                left = mid + 1
            elif target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def searchRange(self, nums, target):
        return (self.firstAppear(nums, target), self.lastAppear(nums, target))

"""
[]
0
[1,1,1,1]
1
[1,2,3,4,5]
3
[1,2,3,4,5]
6
"""
