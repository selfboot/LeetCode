#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Put all i+1 in nums[i]
        nums_len = len(nums)
        for i in range(nums_len):
            # Swap nums[i] to the appropriate position until current
            # nums[i] can't be push to the list, which is <0 or >nums_len
            # By the way, pay attention to situation as [1,1].
            while nums[i] != i + 1 and 0 < nums[i] <= nums_len:
                index = nums[i] - 1
                if nums[index] == nums[i]:
                    break
                nums[i], nums[index] = nums[index], nums[i]
                # nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]

        for i in range(nums_len):
            if nums[i] != i + 1:
                return i + 1

        return nums_len + 1

"""
[]
[1,2,0]
[3,4,-1,1]
[3,4,-1,1,2,2,0,12,3]
"""
