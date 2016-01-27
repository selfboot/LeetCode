#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


class Solution(object):
    def moveZeroes(self, nums):
        # Get sum of zeros
        count = 0
        for num in nums:
            if not num:
                count += 1

        # Move the no-zero number to the right position.
        pos, i = 0, 0
        while pos < len(nums):
            if nums[pos]:
                nums[i] = nums[pos]
                i += 1
            pos += 1

        # Append the zeros
        if count:
            nums[-count:] = [0] * count
        return

"""
[]
[1]
[0]
[0,0,0]
[0,1,0,3,12]
[7,6,5,4,0,4,0,5,6,0,7,0,0]
"""
