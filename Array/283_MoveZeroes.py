#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


class Solution(object):
    def moveZeroes(self, nums):
        # Shift non-zero values as far forward as possible.
        index = 0
        for n in nums:
            if n != 0:
                nums[index] = n
                index += 1

        # Fill remaining space with zeros
        for i in range(index, len(nums)):
            nums[i] = 0

        return

"""
[]
[1]
[0]
[0,0,0]
[0,1,0,3,12]
[7,6,5,4,0,4,0,5,6,0,7,0,0]
"""
