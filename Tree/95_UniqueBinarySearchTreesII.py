#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if not n:
            return [[]]
        roots_lsit = self.root_list(1, n)
        return roots_lsit

    # Get all the roots of the BST's that store values start...end
    def root_list(self, start, end):
        # Null Tree when start > end
        if start > end:
            return []
        # Tree has just a root when start==end
        if start == end:
            return [TreeNode(start)]

        roots = []
        for i in range(start, end + 1):
            # Get all the possible roots and it's left, right childs
            left_childs = self.root_list(start, i-1)
            right_childs = self.root_list(i+1, end)
            # Have no left childs
            if not left_childs and right_childs:
                for child in right_childs:
                    root_node = TreeNode(i)
                    root_node.right = child
                    root_node.left = None
                    roots.append(root_node)
            # Have no right childs
            elif not right_childs and left_childs:
                for child in left_childs:
                    root_node = TreeNode(i)
                    root_node.left = child
                    root_node.right = None
                    roots.append(root_node)
            # Have both left childs and right childs
            else:
                for l_child in left_childs:
                    for r_child in right_childs:
                        root_node = TreeNode(i)
                        root_node.left = l_child
                        root_node.right = r_child
                        roots.append(root_node)

        return roots

"""
0
1
2
3
7
"""
