#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# Refer to:
# https://leetcode.com/discuss/61514/understood-solution-space-without-modifying-explanation


class Solution(object):
    """
    Use two pointers the fast and the slow. The fast one goes forward two steps
    each time, while the slow one goes only step each time.
    In fact, they meet in a circle, the duplicate number
    must be the entry point of the circle when visiting the array from nums[0].
    """
    def findDuplicate(self, nums):
        # assert(len(nums) > 1)
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        target = 0
        while target != slow:
            target = nums[target]
            slow = nums[slow]
        return target

"""
[1]
[1,1]
[1,3,4,5,1,2]
[1,3,4,1,1,2]
"""
