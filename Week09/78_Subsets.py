#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        subsets = []
        n = len(nums)
        nums.sort()
        # We know there are totally 2^n subsets,
        # becase every num may in or not in one subsets.
        # So we check the jth(0<=j<n) bit for every ith(0=<i<2^n) subset.
        # If jth bit is 1, then nums[j] in the subset.
        sum_sets = 2 ** n
        for i in range(sum_sets):
            cur_set = []
            for j in range(n):
                power = 2 ** j
                if i & power == power:
                    cur_set.append(nums[j])

            subsets.append(cur_set)

        return subsets

"""
[0]
[]
[1,2,3,4,7,8]
"""
