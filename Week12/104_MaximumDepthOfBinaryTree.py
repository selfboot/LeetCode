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
            # Then update node_list
            node_scan = node_list[:]
            node_list = []
            for node in node_scan:
                l_child = node.left
                r_child = node.right
                if l_child:
                    node_list.append(l_child)
                if r_child:
                    node_list.append(r_child)
            if node_list:
                depth_count += 1

        return depth_count
"""
[]
[1]
[1,2,3]
[0,1,2,3,4,5,6,null,null,7,null,8,9,null,10]
"""
