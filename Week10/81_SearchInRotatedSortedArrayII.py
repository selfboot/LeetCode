#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """

        nums_size = len(nums)
        start = 0
        end = nums_size - 1

        while start <= end:
            mid = (start + end) / 2
            num_mid = nums[mid]

            # Mid is in the left part of the rotated(if it's rotated) array.
            if num_mid > nums[start]:
                if nums[start] <= target < num_mid:
                    end = mid - 1
                elif target == num_mid:
                    return True
                else:
                    start = mid + 1

            # The array must be rotated, and mid is in the right part
            elif num_mid < nums[start]:
                if num_mid < target <= nums[end]:
                    start = mid + 1
                elif target == num_mid:
                    return True
                else:
                    end = mid - 1

            # Can't make sure whether mid in the left part or right part.
            else:
                # Find the target.
                if target == num_mid:
                    return True
                # Just add start with one until we can make sure.
                # Of course, you can also minus end with one.
                start += 1

        return False

"""
[]
0
[1]
1
[7,8,7,7,7]
8
[7,7,7,8,8]
8
"""
