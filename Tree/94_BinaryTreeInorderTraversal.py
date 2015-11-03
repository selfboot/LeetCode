#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        tree_stack = []
        inorder_tra = []
        while root or tree_stack:
            # Go along the left child
            if root:
                tree_stack.append(root)
                root = root.left
            # Meet a left, go back to the parent node
            else:
                if not tree_stack:
                    root = None
                    continue
                node = tree_stack.pop()
                inorder_tra.append(node.val)
                root = node.right

        return inorder_tra

"""
[]
[1]
[1,2,3,null,null,4,null,null,5]
"""
