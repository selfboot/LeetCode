#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """
    Recursive method: DFS.
    If the current (sub)tree contains both p and q, result is LCA.
    If only one of them is in that subtree, then the result is that one.
    If neither are in that subtree, the result is null/None/nil.
    """
    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        elif left:
            return left
        else:
            return right


class Solution_2(object):
    """
    Iterative method: BFS(DFS is ok too).  According to:
    https://leetcode.com/discuss/64764/java-python-iterative-solution
    """
    def lowestCommonAncestor(self, root, p, q):
        node_stack = [root]
        parent_record = {root: None}
        while p not in parent_record or q not in parent_record:
            node = node_stack.pop()
            if node.left:
                node_stack.append(node.left)
                parent_record[node.left] = node
            if node.right:
                node_stack.append(node.right)
                parent_record[node.right] = node

        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent_record[p]

        while q not in ancestors:
            q = parent_record[q]
        return q
