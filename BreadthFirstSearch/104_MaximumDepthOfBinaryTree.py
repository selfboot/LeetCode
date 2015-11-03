#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        node_list = [root]
        depth_count = 1
        # Breadth-first Search
        while node_list:
            # node_scan: all the nodes in one level.
            # Traverse node_scan and get all the nodes of next level,
            # Then update node_list, and the solution level_traversal
            node_scan = node_list[:]
            node_list = []
            node_level = []
            for node in node_scan:
                l_child = node.left
                r_child = node.right
                if l_child:
                    node_level.append(l_child.val)
                    node_list.append(l_child)
                if r_child:
                    node_level.append(r_child.val)
                    node_list.append(r_child)
            if node_level:
                depth_count += 1

        return depth_count
