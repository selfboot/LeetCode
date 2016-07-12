#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def search(self, nums, target):
        nums_size = len(nums)
        start = 0
        end = nums_size - 1
        while start <= end:
            mid = (start + end) / 2
            num_mid = nums[mid]

            # Mid is in the left part of the rotated(if it's rotated) array.
            if num_mid >= nums[start]:
                if nums[start] <= target < num_mid:
                    end = mid - 1
                elif num_mid == target:
                    return mid
                else:
                    start = mid + 1

            # The array must be rotated, and mid is in the right part
            else:
                if num_mid < target <= nums[end]:
                    start = mid + 1
                elif target == num_mid:
                    return mid
                else:
                    end = mid - 1

        return -1

"""
[]
0
[1]
1
[8,11,13,1,3,4,5,7]
7
[4,5,6,7,8,1,2,3]
8
[5, 1, 3]
1
"""
