#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        hash_dict = {}
        if not nums:
            return False
        len_nums = len(nums)
        for i in range(len_nums):
            num = nums[i]
            if num in hash_dict and i - hash_dict[num] <= k:
                return True
            hash_dict[num] = i
        return False

"""
[]
3
[1,2,3,3]
1
[1,2,3,4,1]
3
"""
