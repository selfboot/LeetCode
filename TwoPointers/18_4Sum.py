#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        solution = []
        length = len(nums)

        for i in range(length - 3):
            # avoid duplicate triplets.
            if i > 0 and nums[i] == nums[i-1]:
                continue

            a = nums[i]
            for j in range(i + 1, length - 2):
                # avoid duplicate triplets.
                if j > i+1 and nums[j] == nums[j-1]:
                    continue

                # Two points which are form head and bottom move toward
                # to make the a + b + c + d == target
                b = nums[j]
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
                        # avoid duplicate triplets.
                        left += 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        right -= 1
                        while right > left and nums[right] == nums[right+1]:
                            right -= 1

        return solution

"""
[]
0
[1, 0, -1, 0, -2, 2]
0
[-2,-2,-2,-2,-1,-1,-1,-1,1,1,1,1,2,2,2,2,0,0,0]
0
"""
