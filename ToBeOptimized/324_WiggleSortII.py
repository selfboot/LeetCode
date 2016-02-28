#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


class Solution(object):
    def wiggleSort(self, nums):
        """
        Clear solutionm, explanation and proof can be found here:
        https://leetcode.com/discuss/76965/3-lines-python-with-explanation-proof
        """
        nums.sort()
        half = (len(nums[::2])) - 1
        # Consider [4,5,5,6]
        # half = (len(nums)+1) // 2
        # nums[::2], nums[1::2] = nums[:half], nums[half:]
        nums[::2], nums[1::2] = nums[half::-1], nums[:half:-1]


class Solution_2(object):
    def wiggleSort(self, nums):
        """
        O(n)-time O(1)-space solution, no sort here.
        According to:
        https://leetcode.com/discuss/77133/o-n-o-1-after-median-virtual-indexing
        """


"""
[4, 5, 5, 6]
[1, 5, 1, 1, 6, 4]
[1, 3, 2, 2, 3, 1]
"""
