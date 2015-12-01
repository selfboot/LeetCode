#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # Postorder Traversal
    def postorderTraversal(self, root):
        if not root:
            return []
        result = []
        node_stack = []
        while root or node_stack:
            if root:
                node_stack.append(root)
                result.append(root.val)
                root = root.right
            else:
                node = node_stack.pop()
                root = node.left
        return result[::-1]

"""
[]
[1, null, 2, 3]
[1, null, 2, 3, null, 4, 5]
"""
