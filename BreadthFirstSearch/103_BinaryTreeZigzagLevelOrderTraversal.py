#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        left2right = 1
        # 1. scan the level from left to right. -1 reverse.
        ans, stack, temp = [], [root], []
        while stack:
            temp = [node.val for node in stack]
            stack = [child for node in stack
                     for child in (node.left, node.right) if child]

            ans += [temp[::left2right]]         # Pythonic way
            left2right *= -1

        return ans

"""
[]
[1]
[1,2,3]
[0,1,2,3,4,5,6,null,null,7,null,8,9,null,10]
"""
