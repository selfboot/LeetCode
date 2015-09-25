#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        solution = []
        length = len(nums)

        for i in range(length - 3):
            a = nums[i]
            for j in range(i + 1, length - 2):
                b = nums[j]

                # Two points which are form head and bottom move toward
                # to make the a + b + c + d == target
                left = j + 1
                right = length - 1
                while left < right:
                    c = nums[left]
                    d = nums[right]
                    if a + b + c + d < target:
                        left += 1
                    elif a + b + c + d > target:
                        right -= 1
                    else:
                        solution.append([a, b, c, d])
                        left += 1
                        right -= 1

        # remove the duplicate list
        no_duplicate = []
        for terms in solution:
            if terms not in no_duplicate:
                no_duplicate.append(terms)

        return no_duplicate
