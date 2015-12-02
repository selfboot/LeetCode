#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        if root.left and root.right:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)
        else:
            return 1

"""
[]
[1]
[1,2,null,3]
[1,2,3,4,null,6,7,5,8]
[1,2,2,3,null,null,3,4,null,null,4]
"""
