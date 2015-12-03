#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        if not points:
            return 0
        # Record all the duplicate points
        replicate = {}
        for point in points:
            replicate[(point.x, point.y)] = replicate.get(
                (point.x, point.y), 0) + 1

        # Get all the different nodes
        diff_points = replicate.keys()
        diff_count = len(diff_points)
        if diff_count == 1:
            return replicate[diff_points[0]]

        maxPoints = 0
        # Get all the different slope's point numbers.
        for i in xrange(diff_count-1):
            slopes = {}
            slope = 0
            for j in range(i+1, diff_count):
                dx = diff_points[i][0] - diff_points[j][0]
                dy = diff_points[i][1] - diff_points[j][1]
                if dx == 0:
                    slope = "#"
                elif dy == 0:
                    slope = 0
                else:
                    slope = float(dy) / dx
                slopes[slope] = (slopes.get(slope, 0) +
                                 replicate[diff_points[j]])

            maxPoints = max(maxPoints,
                            max(slopes.values())+replicate[diff_points[i]])

        return maxPoints

"""
[]
[[1,1]]
[[1,1],[2,2],[1,1],[1,1],[2,2],[2,3]]
"""
