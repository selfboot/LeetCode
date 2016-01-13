#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


class Solution(object):
    # Maintain a minimum window with two indices.
    def minSubArrayLen(self, s, nums):
        if not nums:
            return 0
        start, end, sums, min_len = 0, 0, nums[0], 0
        len_nums = len(nums)
        while end < len_nums:
            # Move the start point to get a bigger sum.
            if sums < s and end + 1 < len_nums:
                end += 1
                sums += nums[end]
            # Move the start point to decrease the window's size.
            if sums >= s:
                if min_len == 0:
                    min_len = end - start + 1
                else:
                    min_len = min(min_len, end - start + 1)
                sums -= nums[start]
                if start < end:
                    start += 1
            # No suitable subarray anymore.
            if end == len_nums - 1 and sums < s:
                break
        return min_len

"""
100
[]
20
[1,3,12,8,3,4,21]
0
[1,1,2]
4
[1,4,4]
"""
