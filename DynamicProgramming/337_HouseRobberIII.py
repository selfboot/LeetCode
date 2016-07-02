#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# @Last Modified time: 2016-07-02 14:38:38


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """ Dynamic programming,  memory dfs search.

    The problem exhibits the feature of optimal substructure and overlapping of subproblems.
        1. Optimal substructure:  If we want to "rob" maximum amount of money
        from current binary tree (rooted at "root"),
        we surely hope that we can do the same to its left and right subtrees.

        2. Overlapping of subproblems: Computed subproblems repeatedly,
        which resulted in bad time performance.

    More details can be found as bellows:
    https://leetcode.com/discuss/91899/step-by-step-tackling-of-the-problem
    """
    cache = {}

    def rob(self, root):
        if not root:
            return 0

        if root in self.cache:
            return self.cache[root]

        # Rob the root node.
        money = root.val
        if root.left:
            money += self.rob(root.left.right) + self.rob(root.left.left)
        if root.right:
            money += self.rob(root.right.left) + self.rob(root.right.right)

        # Do not rob the root node.
        self.cache[root] = max(money, self.rob(root.left) + self.rob(root.right))
        return self.cache[root]

"""
[]
[3,4,5,1,3,null,1]
[3,2,3,null,3,null,1]
"""
