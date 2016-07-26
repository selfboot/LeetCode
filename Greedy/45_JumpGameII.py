#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def jump(self, nums):
        """ When you can reach position i, find the next longest distance you can reach.

        Once we can reach position i, we can find the next longest distance by iterate all
        the position before position i.

        Of course, you can think it as a BFS problem.
        Where nodes in level i are all the nodes that can be reached in i-1th jump.
        For more explnation, goto:
        https://discuss.leetcode.com/topic/3191/o-n-bfs-solution
        """
        if len(nums) == 1:
            return 0

        last = nums[0]
        step = 1
        index = 1
        while last < len(nums) - 1:
            max_distance = 0
            while index <= last:
                if nums[index] + index > max_distance:
                    max_distance = nums[index] + index
                index += 1

            last = max_distance
            step += 1

        return step

"""
[0]
[2,5,0,3]
[2,3,1,1,4]
[3,1,8,1,1,1,1,1,5]
"""
