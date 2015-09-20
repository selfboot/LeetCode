#! /usr/bin/env python
# -*- coding: utf-8 -*-

:w


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {}
        for index1, number1 in enumerate(nums):
            number2 = target - number1
            if number2 in nums_dict:
                return nums_dict[number2] + 1, index1 + 1
            nums_dict[number1] = index1
