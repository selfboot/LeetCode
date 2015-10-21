#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        solution = []
        nums.sort()
        length = len(nums)
        for i in range(length-2):
            # avoid duplicate triplets.
            if i == 0 or nums[i] > nums[i-1]:
                cur_num = nums[i]

                # Keep two points to scan double direction.
                left = i + 1
                right = length - 1
                while left < right:
                    if nums[left] + nums[right] + cur_num < 0:
                        left += 1
                    elif nums[left] + nums[right] + cur_num > 0:
                        right -= 1
                    else:
                        triplet = [cur_num, nums[left], nums[right]]
                        solution.append(triplet)
                        left += 1
                        right -= 1
                        # avoid duplicate triplets.
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1

        return solution

"""
[]
[-1,1,2,-1,-1,0,-2,1,1,3]
"""
