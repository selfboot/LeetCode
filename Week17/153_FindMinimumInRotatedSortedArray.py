#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def findMin(self, nums):
        assert(nums)
        left = 0
        right = len(nums)-1
        while left < right:
            # When there is no rotate, just return self.nums[start]
            if nums[left] < nums[right]:
                return nums[left]

            mid = (left+right) / 2
            if nums[left] < nums[mid]:
                left = mid + 1
            elif nums[left] > nums[mid] and nums[right] > nums[mid]:
                right = mid
            else:
                return nums[right]
        return nums[left]

"""
class Solution(object):
    def findMin(self, nums):
        assert(nums)
        nums_len = len(nums)
        return self.find_minnum(0, nums_len, nums)

    def find_minnum(self, start, end, nums):
        if start + 1 == end:
            return nums[start]

        mid = (start + end) / 2
        mid_num = nums[mid]
        start_num = nums[start]

        # When there is no rotate, should return self.nums[start]
        if start_num < mid_num:
            return min(self.find_minnum(mid, end, nums), nums[start])
        else:
            return self.find_minnum(start+1, mid + 1, nums)
"""

"""
[1]
[1,2]
[3,4,2]
[7,8,9,0,2,4,5]
"""
