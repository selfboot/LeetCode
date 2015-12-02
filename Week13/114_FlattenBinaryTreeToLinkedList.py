#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return None

        self.get_list(root)

    # Flatten the tree to a linked list in-place, and return it's tail.
    def get_list(self, root):
        left_child = root.left
        right_child = root.right

        # Leaf node: do nothing, and the linked list has just one node.
        if not left_child and not right_child:
            return root

        # Have left child node, move it to the next node in the linked list.
        # Flatten the left subtree and then get the tail
        # of the flattened subtree's linked list. Make the right child go after
        # the tail, and flatten the right subtree at last.
        if left_child:
            root.left = None
            root.right = left_child
            left_tail_node = self.get_list(left_child)

            if right_child:
                left_tail_node.right = right_child
                return self.get_list(right_child)
            else:
                return left_tail_node
        # No left child node, just flatten the right node.
        else:
            return self.get_list(right_child)

"""
[]
[1,2,3,null,null,4,5]
[1,2,5,3,4,null,6]
"""
