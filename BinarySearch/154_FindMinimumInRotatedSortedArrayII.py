#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def findMin(self, nums):
        assert(nums)
        left = 0
        right = len(nums) - 1
        # Make sure right is always in the right rotated part.
        # Left can be either in the left part or the minimum part.
        # So, when left and right is the same finally, we find the minimum.
        while left < right:
            # When there is no rotate, just return self.nums[start]
            if nums[left] < nums[right]:
                return nums[left]

            mid = (left + right) / 2
            # mid is in the left part, so move the left point to mid.
            if nums[left] < nums[mid]:
                left = mid + 1
            elif nums[left] > nums[mid]:
                right = mid
            # Can't make sure whether left is in the left part or not.
            # Just move to right for 1 step.
            else:
                left += 1
        return nums[left]

"""
[1]
[7,8,9,9,9,10,2,2,2,3,4,4,5]
"""
