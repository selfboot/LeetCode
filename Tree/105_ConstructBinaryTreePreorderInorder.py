#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        preorder_l = len(preorder)
        inorder_dict = dict(zip(inorder, xrange(preorder_l)))

        if not preorder:
            return None

        return self.recursve_build(
            preorder, 0, preorder_l-1,
            inorder, 0, preorder_l-1,
            inorder_dict)

    def recursve_build(
            self, preorder, p_start, p_end,
            inorder, i_start, i_end, pos_dict):
        # Empty tree
        if p_start > p_end:
            return None
        # Leaf
        if p_start == p_end:
            return TreeNode(preorder[p_start])

        root_val = preorder[p_start]
        root = TreeNode(root_val)

        # Get the left and right part of inorder
        inorder_pos = pos_dict[root_val]
        left_i_start = i_start
        left_i_end = inorder_pos - 1
        right_i_start = inorder_pos + 1
        right_i_end = i_end

        # Get the left and right part of preorder
        p_len = left_i_end - left_i_start
        left_p_start = p_start + 1
        left_p_end = left_p_start + p_len
        right_p_start = left_p_end + 1
        right_p_end = p_end

        # Get the left and right childrens
        root.left = self.recursve_build(
            preorder, left_p_start, left_p_end,
            inorder, left_i_start, left_i_end,
            pos_dict)
        root.right = self.recursve_build(
            preorder, right_p_start, right_p_end,
            inorder, right_i_start, right_i_end,
            pos_dict)

        return root

"""
[]
[]
[10,8,3,2,11,5,7,9]
[3,8,2,10,5,11,7,9]
[7,10,4,3,1,2,8,11]
[4,10,3,1,7,11,8,2]
"""
