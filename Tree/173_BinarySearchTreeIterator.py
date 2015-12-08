#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class BSTIterator(object):
    def __init__(self, root):
        self.root = root
        self.node_stack = []
        self.cur_node = root

    def hasNext(self):
        if self.cur_node or self.node_stack:
            return True
        else:
            return False

    def next(self):
        # inorder traversal
        while self.cur_node:
            self.node_stack.append(self.cur_node)
            self.cur_node = self.cur_node.left

        top = self.node_stack.pop()
        self.cur_node = top.right
        return top.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())

"""
[]
[1]
[10,8,16,2,9,15,17]
"""
