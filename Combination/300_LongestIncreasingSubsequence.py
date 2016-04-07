#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


class Solution(object):
    """
    Clear explanation is here:
    https://leetcode.com/discuss/67687/c-o-nlogn-solution-with-explainations-4ms
    https://leetcode.com/discuss/67643/java-python-binary-search-o-nlogn-time-with-explanation

    The key to the solution is: build a ladder for numbers: dp.
    dp[i]: the smallest num of all increasing subsequences with length i+1.
    When a new number x comes, compare it with the number in each level:
        1. If x is larger than all levels, append it, increase the size by 1
        2. If dp[i-1] < x <= dp[i], update dp[i] with x.

    For example, say we have nums = [4,5,6,3],
    then all the available increasing subsequences are:

    len = 1: [4], [5], [6], [3]   => dp[0] = 3
    len = 2: [4, 5], [5, 6]       => dp[1] = 5
    len = 3: [4, 5, 6]            => dp[2] = 6
    """
    def lengthOfLIS(self, nums):
        dp = [0] * len(nums)
        size = 0
        for n in nums:
            # Binary search here.
            left, right = 0, size
            while left < right:
                mid = (left + right) / 2
                if dp[mid] < n:
                    left = mid + 1
                else:
                    right = mid
            # Append the next number
            dp[right] = n
            # Update size
            if right == size:
                size += 1

        return size

"""
[]
[3]
[1,1,1,1]
[10,9,2,5,3,7,101,18]
"""
