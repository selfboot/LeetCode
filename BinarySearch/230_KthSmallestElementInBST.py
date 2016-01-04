#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# Refer to:
# https://leetcode.com/discuss/43771/implemented-java-binary-search-order-iterative-recursive
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Binary search iterative
class Solution(object):
    def kthSmallest(self, root, k):
        count = self.get_nodes(root.left)
        while count + 1 != k:
            if count + 1 < k:
                root = root.right
                k = k - count - 1
            else:
                root = root.left
            count = self.get_nodes(root.left)
        return root.val

    def get_nodes(self, root):
        if not root:
            return 0
        return 1 + self.get_nodes(root.left) + self.get_nodes(root.right)


# Binary search recursive
class Solution_2(object):
    def kthSmallest(self, root, k):
        count = self.get_nodes(root.left)
        if count+1 < k:
            return self.kthSmallest(root.right, k-count-1)
        elif count+1 == k:
            return root.val
        else:
            return self.kthSmallest(root.left, k)

    def get_nodes(self, root):
        if not root:
            return 0
        return 1 + self.get_nodes(root.left) + self.get_nodes(root.right)


# DFS in-order iterative:
class Solution_3(object):
    def kthSmallest(self, root, k):
        node_stack = []
        count, result = 0, 0
        while root or node_stack:
            if root:
                node_stack.append(root)
                root = root.left
            else:
                if node_stack:
                    root = node_stack.pop()
                    result = root.val
                    count += 1
                    if count == k:
                        return result
                    root = root.right

        return -1   # never hit if k is valid


# DFS in-order recursive:
class Solution_4(object):
    def kthSmallest(self, root, k):
        self.k = k
        self.num = 0
        self.in_order(root)
        return self.num

    def in_order(self, root):
        if root.left:
            self.in_order(root.left)
        self.k -= 1
        if self.k == 0:
            self.num = root.val
            return
        if root.right:
            self.in_order(root.right)


# DFS in-order recursive, Pythonic approach with generator:
class Solution_5(object):
    def kthSmallest(self, root, k):
        for val in self.in_order(root):
            if k == 1:
                return val
            else:
                k -= 1

    def in_order(self, root):
        if root:
            for val in self.in_order(root.left):
                yield val
            yield root.val
            for val in self.in_order(root.right):
                yield val

"""
[1]
1
[3,1,4,null,2]
1
[10,8,6,9,14,12,15,null,null,null,null,11]
4
[10,8,6,9,14,12,15,null,null,null,null,11]
5
"""
