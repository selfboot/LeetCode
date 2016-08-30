#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def sortColors(self, nums):
        len_n = len(nums)
        # pos_put_0: next position to put 0
        # pos_put_2: next position to put 2
        pos_put_0 = 0
        pos_put_2 = len_n - 1
        index = 0
        while index <= pos_put_2:
            if nums[index] == 0:
                nums[index], nums[pos_put_0] = nums[pos_put_0], nums[index]
                pos_put_0 += 1
                index += 1

            elif nums[index] == 2:
                nums[index], nums[pos_put_2] = nums[pos_put_2], nums[index]
                pos_put_2 -= 1

            else:
                index += 1

"""
[0]
[1,0]
[0,1,2]
[1,1,1,2,0,0,0,0,2,2,1,1,2]
"""
