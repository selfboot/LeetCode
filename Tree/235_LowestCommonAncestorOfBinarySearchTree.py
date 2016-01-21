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
    # Easy to understand
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


class Solution_2(object):
    """
    One elegant code, some puzzling but short code. according to:
    https://leetcode.com/discuss/44959/3-lines-with-o-1-space-1-liners-alternatives
    Just walk down from the whole tree's root as long as
    both p and q are in the same subtree
    """
    def lowestCommonAncestor(self, root, p, q):
        while (root.val - p.val) * (root.val - q.val) > 0:
            root = (root.left, root.right)[p.val > root.val]
        return root
