#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        no_dup_nums = [nums[0]]
        for num in nums:
            if num != no_dup_nums[-1]:
                no_dup_nums.append(num)

        left = 0
        right = len(no_dup_nums)-1
        while left < right:
            # When there is no rotate, just return self.nums[start]
            if no_dup_nums[left] < no_dup_nums[right]:
                return no_dup_nums[left]

            mid = (left+right) / 2
            if no_dup_nums[left] < no_dup_nums[mid]:
                left = mid + 1
            elif (no_dup_nums[left] > no_dup_nums[mid] and
                    no_dup_nums[right] > no_dup_nums[mid]):
                right = mid
            else:
                return no_dup_nums[right]
        return no_dup_nums[left]

"""
[1]
[7,8,9,9,9,10,2,2,2,3,4,4,5]
"""
