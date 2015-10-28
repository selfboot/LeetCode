#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        length = len(nums)

        # Get all the two sums and their two addend's index.
        two_sums_dict = {}
        for i in range(length):
            for j in range(i+1, length):
                two_sums = nums[i] + nums[j]
                if two_sums not in two_sums_dict:
                    two_sums_dict[two_sums] = []
                two_sums_dict[two_sums].append([i, j])

        sums_list = two_sums_dict.keys
        sums_list.sort()
        solution = []







"""
[]
0
[1, 0, -1, 0, -2, 2]
0
[1,1,1,1,0,0,0,0,-1,-1,-1,-1]
0
"""
