#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        left2right = -1
        # Get the first level, there's just a root node.
        node_list = [root]
        level_traversal = [[root.val]]

        # Breadth-first Search
        while node_list:
            # left2right:
            # 1, scan the childrens of node in node_list from left to right;
            # -1, scan the childrens of node in node_list from right to left.
            node_scan = node_list[::-1]

            node_list = []
            node_level = []
            for node in node_scan:
                l_child = node.left
                r_child = node.right

                if l_child:
                    level_len = len(node_level)
                    node_level.append(l_child.val)
                    node_list.append(l_child)

                if r_child:
                    # If scan from right to left, for every node in node_list,
                    # Insert right child before left child(if have one).
                    level_len = len(node_level)
                    if l_child:
                        node_level.insert(left2right + level_len, r_child.val)
                        node_list.insert(left2right + level_len, r_child)
                    else:
                        node_level.append(r_child.val)
                        node_list.append(r_child)

            if node_level:
                level_traversal.append(node_level)
            left2right *= -1

        return level_traversal

"""
[]
[1]
[1,2,3]
[0,1,2,3,4,5,6,null,null,7,null,8,9,null,10]
"""
