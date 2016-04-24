#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []

        cur_level, ans = [root], []

        # Breadth-first Search, Pythonic way.
        while cur_level:
            ans.append([node.val for node in cur_level])
            cur_level = [kid for n in cur_level
                         for kid in (n.left, n.right) if kid]

        return ans

"""
[]
[1]
[1,2,3]
[3,9,20,null,null,15,7]
"""
