#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def trap(self, height):
        """ For each bar, calculate its left and right highest elevation.

        Then calculating total area by sum of each bar's height*width.

        There is a brilliant solution in discuss:
        https://discuss.leetcode.com/topic/5125/sharing-my-simple-c-code-o-n-time-o-1-space
        """

        # Get the left highest elevation of each bar
        left_side = []
        max_high = 0
        for high in height:
            if high > max_high:
                max_high = high
            left_side.append(max_high)

        # Get the right highest elevation of each bar
        right_side = []
        max_high = 0
        for high in height[::-1]:
            if high > max_high:
                max_high = high
            right_side.append(max_high)

        # Scan each bar and get the water
        water = 0
        length = len(height)
        for i in range(length):
            min_side = min(left_side[i], right_side[length - i - 1])
            if min_side > height[i]:
                water += min_side - height[i]

        return water

"""
[]
[3,0,0,3]
[1,1,1,2,2,1,1]
[0,1,0,2,1,0,1,3,2,1,2,1]
"""
