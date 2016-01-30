#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


class NumArray(object):
    def __init__(self, nums):
        length = len(nums)
        # dp[i]: sum of nums[0] to nums[i]
        # To process dp[0] easily we add 1 to length
        self.dp = [0] * (length+1)
        for i, n in enumerate(nums):
            self.dp[i] = self.dp[i-1] + n

    def sumRange(self, i, j):
        # sum of elements nums[i..j], inclusive.
        return self.dp[j] - self.dp[i-1]

# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)
