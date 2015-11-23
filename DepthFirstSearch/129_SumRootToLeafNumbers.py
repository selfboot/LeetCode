#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """
    Depth First Search
    """
    def sumNumbers(self, root):
        node_stack = []
        path_sum = 0
        # Keep the path number from root to the current node.
        cur_node_num = 0

        while root or node_stack:
            if root:
                cur_node_num = cur_node_num * 10 + root.val
                node_stack.append([root, cur_node_num])
                root = root.left

            else:
                if node_stack:
                    pop_record = node_stack.pop()
                    root = pop_record[0].right
                    cur_node_num = pop_record[1]
                    # Meet a leaf node
                    if not pop_record[0].left and not root:
                        path_sum += cur_node_num

                else:
                    break
        return path_sum

"""
[]
[1,2,3]
[1,null,2,3,null,null,4,5,6]
"""
