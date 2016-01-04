#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# According to:
# https://leetcode.com/discuss/43248/boyer-moore-majority-vote-algorithm-and-my-elaboration


class Solution(object):
    def majorityElement(self, nums):
        if not nums:
            return []
        candidate_1, candidate_2 = 0, 1
        count_1, count_2 = 0, 0
        for num in nums:
            if num == candidate_1:
                count_1 += 1
            elif num == candidate_2:
                count_2 += 1
            elif not count_1:
                candidate_1, count_1 = num, 1
            elif not count_2:
                candidate_2, count_2 = num, 1
            else:
                count_1 -= 1
                count_2 -= 1
        result = []
        for num in [candidate_1, candidate_2]:
            if nums.count(num) > len(nums) / 3:
                result.append(num)
        return result
"""
[]
[0,0,0]
[1,2,2,3,3,1,1,1]
[2,2,2,3,3,4,3,2]
[1,1,2]
[3,0,3,4]
"""
