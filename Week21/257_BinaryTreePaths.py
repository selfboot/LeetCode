#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        if not root:
            return []
        node_stack = [[root, str(root.val)]]
        path_str = []
        while node_stack:
            node, path = node_stack.pop()
            if node.left:
                new_path = path + "->" + str(node.left.val)
                node_stack.append([node.left, new_path])
            if node.right:
                new_path = path + "->" + str(node.right.val)
                node_stack.append([node.right, new_path])
            if not node.left and not node.right:
                path_str.append(path)
        return path_str

"""
[]
[1]
[1,2,3,4,null,null,null,5]
"""
