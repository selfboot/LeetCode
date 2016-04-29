#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        return self.helper(root, root)

    # If two nodes are symmetric
    def helper(self, lNode, rNode):
        if not lNode or not rNode:
            return lNode == rNode
        if lNode.val != rNode.val:
            return False
        return (self.helper(lNode.left, rNode.right) and
                self.helper(lNode.right, rNode.left))

"""
[]
[1]
[1,2,3]
[1,2,2,3,4,4,3]
[1,2,2,null,3,null,3]
"""
