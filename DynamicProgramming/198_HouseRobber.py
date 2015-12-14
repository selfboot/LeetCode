#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    # Dynamic Programming
    def rob(self, nums):
        if not nums:
            return 0
        pre_rob = 0
        pre_not_rob = 0
        for num in nums:
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
