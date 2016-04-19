#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        if not root:
            return False

        root_val = root.val
        if root.left and self.hasPathSum(root.left, sum-root_val):
            return True
        if root.right and self.hasPathSum(root.right, sum-root_val):
            return True
        if not root.left and not root.right and sum == root.val:
            return True
        return False

"""
[]
0
[1,2,3,4,null,6,7,5,8]
15
[1,2,2,3,null,null,3,4,null,null,4]
9
"""
