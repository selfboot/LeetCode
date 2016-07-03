#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# @Last Modified time: 2016-07-03 09:06:53


class Solution(object):
    """ Dynamic Programming

    For an increasingly sorted array of integers a[0 .. n-1]
    dp[n]: the length of the largest divisible subset whose largest number is a[n]
    Then dp[n+1] = max{ 1 + T[i] if a[n+1] % a[i] == 0 else 1 } for i in [0:n+1].
    For the final result we will need to maintain a backtrace array for the answer.

    For more details, look at:
    https://leetcode.com/discuss/110914/c-solution-with-explanations
    """
    def largestDivisibleSubset(self, nums):
        if not nums:
            return []
        nums.sort()
        length = len(nums)
        dp = [1] * length

        pre_num = [0] * length
        max_len, max_pos = 1, 0
        for i in xrange(1, length):
            for j in xrange(i - 1, -1, -1):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    pre_num[i] = j
                    max_pos = i if max_len < dp[i] else max_pos
                    max_len = max(max_len, dp[i])

        ans = []
        for i in range(max_len):
            ans.append(nums[max_pos])
            max_pos = pre_num[max_pos]
        return ans


"""
[]
[1]
[2,3]
[1,2,4,8]
[54,3,24,18,6,9,12]
[2,3,18,24,72,108,216]
"""
