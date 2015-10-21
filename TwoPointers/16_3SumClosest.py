#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        min_distance = 2 ** 31 - 1
        length = len(nums)
        # keep the sum of three nums
        solution = 0
        for i in range(length-2):
            cur_num = nums[i]
            left = i + 1
            right = length - 1
            while left < right:
                left_num = nums[left]
                right_num = nums[right]
                three_sum = cur_num + left_num + right_num

                # the right point go back
                if three_sum > target:
                    right -= 1
                    if min_distance > three_sum - target:
                        solution = three_sum
                        min_distance = three_sum - target
                # the left point go forward
                elif three_sum < target:
                    if min_distance > target - three_sum:
                        solution = three_sum
                        min_distance = target - three_sum
                    left += 1
                else:
                    return three_sum

        return solution

"""
[0,0,0]
1
[-1,-1,-1,-2,-3,1,2]
5
"""
