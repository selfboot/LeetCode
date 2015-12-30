#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        size_1 = (C-A) * (D-B)
        size_2 = (G-E) * (H-F)
        left = max(A, E)
        bottom = max(B, F)
        right = min(C, G)
        top = min(D, H)

        # There is an area coverd by both the two rectangle
        if left < right and bottom < top:
            return size_1 + size_2 - (top-bottom) * (right-left)
        else:
            return size_1 + size_2

"""
-2
-2
2
2
-2
-2
2
2
0
0
0
0
-1
-1
1
1
"""
