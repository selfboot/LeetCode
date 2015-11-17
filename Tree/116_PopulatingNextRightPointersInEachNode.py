#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        if not root:
            return None

        cur_head = root
        next_head = None

        # Breadth-first Scan
        while cur_head:
            if cur_head.left:
                # Get the next level's head
                if not next_head:
                    next_head = cur_head.left
                cur_head.left.next = cur_head.right
            if cur_head.right and cur_head.next:
                cur_head.right.next = cur_head.next.left

            cur_head = cur_head.next

            # Go to next level.
            if not cur_head:
                cur_head = next_head
                next_head = None

""" Readable implementation
class Solution(object):
    def connect(self, root):

        # For all the non-empty nodes:
        #     node.left.next = node.right
        #     node.right.next = node.next.left(if node.next not none)

        if not root:
            return None
        if root.left:
            root.left.next = root.right
        if root.next and root.right:
            root.right.next = root.next.left

        self.connect(root.left)
        self.connect(root.right)
"""

"""
[0]
[1,2,3]
[0,1,2,3,4,5,6]
"""
