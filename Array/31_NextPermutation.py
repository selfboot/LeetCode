#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def nextPermutation(self, nums):
        length = len(nums)
        index = length - 1

        """
        Scan from the end of nums and get nums[index],
        find one pair which nums[mark] > nums[mark - 1],
        then swap the smallest number in nums[mark:] and nums[mark - 1].
        Finally sort nums[mark:] and we will slove the problem.
        """
        while index >= 1:
            if nums[index] > nums[index - 1]:
                for i in range(length - 1, index - 1, -1):
                    if nums[i] > nums[index - 1]:
                        nums[i], nums[index - 1] = nums[index - 1], nums[i]
                        nums[index:] = sorted(nums[index:])
                        return
            else:
                index -= 1

        # Nums is in descending order, just reverse it.
        nums.reverse()

"""
[]
[1]
[1,2,3]
[3,2,1]
[1,1,2,2,4,5,5]
"""
