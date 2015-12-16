#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # Breadth First Search
    def rightSideView(self, root):
        if not root:
            return []
        cur_level = [root]
        next_level = []
        result = []
        while cur_level:
            for node in cur_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            result.append(cur_level[-1].val)
            cur_level = next_level
            next_level = []
        return result

"""
[]
[1,2,3]
[1,2,3,null,4,null,5]
"""
