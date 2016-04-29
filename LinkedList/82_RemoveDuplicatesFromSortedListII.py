#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# @Last Modified time: 2016-04-29 17:15:38


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Recursively
class Solution(object):
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head
        if head.val == head.next.val:
            while head.next and head.val == head.next.val:
                head = head.next
            return self.deleteDuplicates(head.next)
        else:
            head.next = self.deleteDuplicates(head.next)
            return head


# Iteraively
class Solution_2(object):
    def deleteDuplicates(self, head):
        cur = pre_head = ListNode(0)
        while head:
            if head.next and head.val == head.next.val:
                # Skip the duplicated nodes.
                while head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
            # we can make sure head is one single node here.
            else:
                cur.next = head
                cur = cur.next
                head = head.next
        cur.next = None     # Make sure the cur here is the tail: [1,2,2]
        return pre_head.next

"""
[]
[1]
[1,2,2]
[3,3,3,3,3]
[1,1,1,2,3,4,4,4,4,5]
"""
