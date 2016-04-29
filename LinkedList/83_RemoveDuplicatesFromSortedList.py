#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# @Last Modified time: 2016-04-29 16:18:37


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Recursively
class Solution_2(object):
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head
        head.next = self.deleteDuplicates(head.next)
        return head.next if head.val == head.next.val else head


# Iteratively
class Solution(object):
    def deleteDuplicates(self, head):
        cur = head
        while cur:
            # Skip all the duplicated nodes of cur.
            while cur.next and cur.val == cur.next.val:
                cur.next = cur.next.next
            # No duplicated nodes, move cur to next node
            cur = cur.next

        return head

"""
[]
[1]
[3,3,3,3,3]
[1,1,1,2,3,4,4,4,4,5]
"""
