#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        solution = []
        sorted_nums = sorted(nums)
        length = len(sorted_nums)
        for i in range(length):
            cur_num = sorted_nums[i]
            left = i + 1
            right = length - 1
            while left < right:
                if sorted_nums[left] + sorted_nums[right] + cur_num < 0:
                    left += 1
                elif sorted_nums[left] + sorted_nums[right] + cur_num > 0:
                    right -= 1
                else:
                    triplet = [sorted_nums[left], cur_num, sorted_nums[right]]
                    solution.append(sorted(triplet))
                    left += 1
                    right -= 1

        solution_unique = []
        for sol in solution:
            if sol not in solution_unique:
                solution_unique.append(sol)
        return solution_unique
