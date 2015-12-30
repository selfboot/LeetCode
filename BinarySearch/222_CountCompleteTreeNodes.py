#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# Refer to:
# https://leetcode.com/discuss/38930/concise-java-solutions-o-log-n-2

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def countNodes(self, root):
        if not root:
            return 0
        node_nums = 0
        tree_height = self.getHeight(root)
        while root:
            if self.getHeight(root.right) == tree_height - 1:
                # root.left's subtree is a full complete binary tree
                # and it's height is tree_height-1
                node_nums += 1 << tree_height
                root = root.right
            else:
                # root.right's subtree is a full complete binary tree
                # and it's height is tree_height-2
                node_nums += 1 << (tree_height-1)
                root = root.left

            tree_height -= 1

        return node_nums

    # Get complete BT's height, assume the root is height 0, increment then.
    def getHeight(self, root):
        if not root:
            return -1
        height = 0
        while root.left:
            root = root.left
            height += 1
        return height

"""
[]
[1]
[1,2,3,4,5,6,7,8,9,10]
[1,2,3,4,5]
"""
