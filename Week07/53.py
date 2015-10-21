#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_len = len(nums)
        dp = [-1 for i in range(num_len)]
        max_sum = dp[num_len - 1] = nums[num_len - 1]
        for i in range(num_len - 2, -1, -1):
            if nums[i] + dp[i + 1] > nums[i]:
                dp[i] = nums[i] + dp[i + 1]
            else:
                dp[i] = nums[i]

            if dp[i] > max_sum:
                max_sum = dp[i]

        return max_sum

"""
[-1]
[1]
[-2,1,-3,4,-1,2,1,-5,4]
"""
