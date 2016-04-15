#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution_2(object):
    # Hashtable
    def twoSum(self, nums, target):
        nums_dict = {}
        for index1, number1 in enumerate(nums):
            number2 = target - number1
            if number2 in nums_dict:
                return nums_dict[number2] + 1, index1 + 1
            nums_dict[number1] = index1

"""
[1,2]
3
[3,2,4]
6
"""
