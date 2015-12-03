#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        start = dummy
        while head:
            cur_node = head
            head = head.next
            # Don't need to scan from head of the sorted list every time.
            if start.val > cur_node.val:
                start = dummy
            # Find the insert position.
            while start.next and start.next.val < cur_node.val:
                start = start.next
            # Insert the current node.
            cur_node.next = start.next
            start.next = cur_node

        return dummy.next
"""
[]
[1]
[1,2]
[5,1,2]
[5,1,2,3]
"""
