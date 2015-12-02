#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        return self.depth_sub(root) != -1

    # When get depth of subtree, we check if it's balanced at the same time.
    # if subtree of one node is not balanced, then it's height is -1
    def depth_sub(self, root):
        if not root:
            return 0

        left = self.depth_sub(root.left)
        right = self.depth_sub(root.right)

        if abs(left - right) > 1 or left == -1 or right == -1:
            return -1

        return 1 + max(left, right)

"""
class Solution(object):
    def isBalanced(self, root):
        if not root:
            return True

        if abs(self.depth(root.left) - self.depth(root.right)) > 1:
            return False
        if not self.isBalanced(root.left) or not self.isBalanced(root.right):
            return False
        return True

    # Get the tree's height
    def depth(self, root):
        if not root:
            return 0

        node_list = [root]
        depth_count = 1
        # Breadth-first Search
        while node_list:
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

    # Get the tree's height: recursion
    def depth_two(self, root):
        if not root:
            return 0
        if root.left or root.right:
            return 1 + max(self.depth(root.left), self.depth(root.right))
        else:
            return 1
"""
"""
[]
[1]
[1,2,null,3]
[1,2,3,4,null,6,7,5,8]
[1,2,2,3,null,null,3,4,null,null,4]
"""
