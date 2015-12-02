#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows:
            return []
        triangle = [[0 for j in range(i+1)] for i in range(numRows)]
        triangle[0] = [1]

        for i in range(1, numRows):
            one_row = []
            for j in range(i+1):
                num = 0
                if j < i:
                    num = triangle[i-1][j]
                if i > j-1 >= 0:
                    num += triangle[i-1][j-1]
                one_row.append(num)

            triangle[i] = one_row

        return triangle

"""
0
10
"""
