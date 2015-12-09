#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def maxPathSum(self, root):
        result = []
        self.max_path(root, result)
        return result[0]

    """
    Return value root_path_sum: the max sum of the path
    which go from any sub-nodes to the current root.
    So we can extend the path go through the current root's parent.
    At the same time, we update the final max_path_sum
    with the root_path_sum and a path go through root's left and right
    """
    def max_path(self, root, max_path_sum):
        if not root:
            return 0

        left_path_sum = self.max_path(root.left, max_path_sum)
        right_path_sum = self.max_path(root.right, max_path_sum)

        # Get the max sum of path that fomr sub-nodes to current root
        max_path = max(left_path_sum, right_path_sum)
        root_path_sum = max(max_path+root.val, root.val)

        # update the max path sum
        gothrough_root_path = left_path_sum + right_path_sum + root.val
        if not max_path_sum:
            max_path_sum.append(max(root_path_sum, gothrough_root_path))
        else:
            max_path_sum[0] = max(root_path_sum, gothrough_root_path,
                                  max_path_sum[0])
        return root_path_sum

"""
[]
[-3]
[1,2,3]
[1,2,3,4,5,-5,-4]
[-6,-2,3,4,5,-5,-4]
"""
