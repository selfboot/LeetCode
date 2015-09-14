#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        left = 0
        right = length - 1
        max_area = 0
        while left < right:
            area = (right - left) * min(height[left], height[right])
            max_area = max(max_area, area)

            if height[left] < height[right]:
                min_height = height[left]
                left += 1
                while height[left] < min_height:
                    left += 1

            else:
                min_height = height[right]
                right -= 1
                while height[right] < min_height:
                    right -= 1

        return max_area
