#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    # Easy to understand: recursively.
    def permute(self, nums):
        ans = []
        self.dfs(nums, [], ans)
        return ans

    def dfs(self, nums, path, ans):
        if not nums:
            ans.append(path)
        for i, n in enumerate(nums):
            self.dfs(nums[:i] + nums[i + 1:], path + [n], ans)


class Solution_2(object):
    # Pythonic way.  recursively.
    # According to: https://leetcode.com/discuss/42550/one-liners-in-python
    def permute(self, nums):
        return [[n] + p
                for i, n in enumerate(nums)
                for p in self.permute(nums[:i] + nums[i + 1:])] or [[]]

"""
[]
[1]
[1,2,3]
"""
