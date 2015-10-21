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

        # To find the biggest container, we recursively find a container
        # which is much bigger than what we have find before.
        while left < right:
            area = (right - left) * min(height[left], height[right])
            max_area = max(max_area, area)

            # To get a bigger container, we move point(lower height) to right
            if height[left] < height[right]:
                min_height = height[left]
                left += 1
                while height[left] < min_height:
                    left += 1

            # To get a bigger container, we move point(lower height) to left
            else:
                min_height = height[right]
                right -= 1
                while height[right] < min_height:
                    right -= 1

        return max_area

"""
[1,1]
[1,2,3,4,8,7,6,5]
[]
"""
