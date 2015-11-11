#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first_occ = 0
        nums_l = len(nums)
        count = 0
        while first_occ < nums_l:
            # The last single number occurence only once.
            if first_occ == nums_l - 1:
                nums[count] = nums[first_occ]
                count += 1
                break

            # Always keep the first occurence of a number
            first_num = nums[first_occ]
            second_num = nums[first_occ+1]
            # Move the number occurence only once to it's position
            if first_num != second_num:
                nums[count] = first_num
                count += 1
                first_occ += 1
                continue

            # Move the number occur twice to their positions
            if first_num == second_num:
                nums[count] = first_num
                nums[count+1] = second_num
                next_occ = first_occ+2
                while next_occ < nums_l and nums[next_occ] == second_num:
                    next_occ += 1
                count += 2
                first_occ = next_occ
        return count


"""
[]
[1,1,1,1,2,2,2,3,3,3,4,5,6,6,6,7]
"""
