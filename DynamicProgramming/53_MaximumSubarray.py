#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    # O(n) space
    def maxSubArray(self, nums):
        num_len = len(nums)
        # dp[i]: Largest sum of contiguous subarray start from i
        dp = [-1] * num_len
        max_sum = dp[num_len - 1] = nums[num_len - 1]

        for i in range(num_len - 2, -1, -1):
            dp[i] = max(nums[i], dp[i+1]+nums[i])
            max_sum = max(dp[i], max_sum)

        return max_sum


class Solution_2(object):
    # DP same with the previous, but O(1) space
    def maxSubArray(self, nums):
        num_len = len(nums)
        max_sum = pre_sum = nums[num_len - 1]

        for i in range(num_len - 2, -1, -1):
            pre_sum = max(nums[i], pre_sum+nums[i])
            max_sum = max(pre_sum, max_sum)

        return max_sum

"""
[-1]
[1]
[-9,-2,-3,-5,-3]
[-2,1,-3,4,-1,2,1,-5,4]
"""
