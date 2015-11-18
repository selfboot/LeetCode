#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # When do inorder traversal, the val growth bigger.
        node_stack = []
        max_val = "init"
        while root or node_stack:
            if not root:
                if not node_stack:
                    return True
                node = node_stack.pop()
                if max_val == "init" or node.val > max_val:
                    max_val = node.val
                else:
                    return False
                root = node.right
            else:
                node_stack.append(root)
                root = root.left
        return True

"""
[]
[1]
[1,null,2,3]
[10,5,15,null,null,6,20]
"""
