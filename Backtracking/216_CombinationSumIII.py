#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


class Solution(object):
    def combinationSum3(self, k, n):
        self.combination = []
        self._combination_sum(k, n, [])
        return self.combination

    def _combination_sum(self, k, n, nums):
        if not k:
            if sum(nums) == n:
                # self.combination.append(nums)
                # Warning: nums[:] get a new list.
                # If not, we will get self.combination = [[], [], ...] finally.
                self.combination.append(nums[:])
            else:
                return

        # Get the new num from start
        start = 1
        if nums:
            start = nums[-1] + 1
        for i in range(start, 10):
            cur_sum = sum(nums) + i
            if cur_sum <= n:
                nums.append(i)
                self._combination_sum(k - 1, n, nums)
                del nums[-1]    # Backtracking
            else:
                break

"""
0
3
3
7
9
45
"""
