#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    # iteratively
    def inorderTraversal(self, root):
        tree_stack = []
        inorder_tra = []
        while root or tree_stack:
            # Go along the left child
            if root:
                tree_stack.append(root)
                root = root.left
            # Meet a left, go back to the parent node
            else:
                node = tree_stack.pop()
                inorder_tra.append(node.val)
                root = node.right

        return inorder_tra


class Solution_2(object):
    # recursively
    def inorderTraversal(self, root):
        inorder_tra = []
        self.helper(root, inorder_tra)
        return inorder_tra

    def helper(self, root, inorder_tra):
        if root:
            self.helper(root.left, inorder_tra)
            inorder_tra.append(root.val)
            self.helper(root.right, inorder_tra)

"""
[]
[1]
[1,2,3,null,null,4,null,null,5]
"""
