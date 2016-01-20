#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


class Solution(object):
    # Dynamic Programming
    def rob(self, nums):
        if not nums:
            return 0
        # We can break the circle according to whether rob house 0 or not.
        return max(self.rob_line(nums[1:]),  # Not rob first house
                   self.rob_line(nums[2:-1]) + nums[0])  # Rob first house

    def rob_line(self, nums):
        if not nums:
            return 0
        pre_rob = nums[0]
        pre_not_rob = 0
        for num in nums[1:]:
            cur_rob = pre_not_rob + num
            cur_not_rob = max(pre_rob, pre_not_rob)
            pre_rob = cur_rob
            pre_not_rob = cur_not_rob
        return max(pre_rob, pre_not_rob)

"""
[]
[1,2]
[12, 1,1,12,1]
"""
