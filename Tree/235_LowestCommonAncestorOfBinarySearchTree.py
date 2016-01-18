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
    def lowestCommonAncestor(self, root, p, q):
        min_val = min(p.val, q.val)
        max_val = max(p.val, q.val)
        while root:
            value = root.val
            if min_val <= value <= max_val:
                return root
            elif max_val < value:
                root = root.left
            else:
                root = root.right
        return None
