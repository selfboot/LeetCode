#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        return self.get_root(nums)

    def get_root(self, nums):
        if not nums:
            return None
        nums_l = len(nums)
        if nums_l == 1:
            return TreeNode(nums[0])

        # Find the root of the current balanced BST,
        # which is conconverted by the current nums.
        """
        height = 1                  # The height of the balanced BST
        while nums_l > 2 ** height - 1:
            height += 1

        half_child_leaves = 2 ** (height-1) / 2
        full_level_nodes = 2 ** (height-1) - 1
        left_child_nodes = nums_l - full_level_nodes - half_child_leaves
        left_child_nodes = 0 if left_child_nodes < 0 else left_child_nodes
        root_index = full_level_nodes / 2 + left_child_nodes
        """
        root_index = nums_l / 2
        root = TreeNode(nums[root_index])
        root.left = self.get_root(nums[:root_index])
        root.right = self.get_root(nums[root_index+1:])
        return root

"""
[]
[1,3,5,7]
[1,3,5,7,9,11]
[1,3,5,7,9,11,13]
"""
