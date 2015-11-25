#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None
        inorder_l = len(inorder)
        inorder_dict = dict(zip(inorder, xrange(inorder_l)))
        return self.recursve_build(
            inorder, 0, inorder_l - 1,
            postorder, 0, inorder_l - 1,
            inorder_dict)

    def recursve_build(
            self, inorder, i_start, i_end,
            postorder, p_start, p_end, inorder_dict):
        # Empty tree
        if i_start > i_end:
            return None
        if i_start == i_end:
            return TreeNode(inorder[i_start])

        root_val = postorder[p_end]
        root = TreeNode(root_val)

        # Get the left and right part of inorder
        inorder_pos = inorder_dict[root_val]
        l_i_start = i_start
        l_i_end = inorder_pos - 1
        r_i_start = inorder_pos + 1
        r_i_end = i_end

        # Get the left and right part of postorder
        l_p_len = l_i_end - l_i_start
        l_p_start = p_start
        l_p_end = l_p_start + l_p_len
        r_p_start = l_p_end + 1
        r_p_end = p_end - 1

        # Get the left and right childrens
        root.left = self.recursve_build(
            inorder, l_i_start, l_i_end,
            postorder, l_p_start, l_p_end,
            inorder_dict)
        root.right = self.recursve_build(
            inorder, r_i_start, r_i_end,
            postorder, r_p_start, r_p_end,
            inorder_dict)
        return root
"""
[]
[]
[10,8,3,2,11,5,7,9]
[3,8,2,10,5,11,7,9]
[7,10,4,3,1,2,8,11]
[4,10,3,1,7,11,8,2]
"""
