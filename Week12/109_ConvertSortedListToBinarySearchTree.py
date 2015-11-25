#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
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
