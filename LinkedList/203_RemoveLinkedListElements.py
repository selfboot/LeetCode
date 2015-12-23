#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        pre_node = dummy = ListNode(0)
        while head:
            if head.val == val:
                pre_node.next = None
            else:
                pre_node.next = head
                pre_node = head
            head = head.next
        return dummy.next

"""
[]
1
[1,1,1]
1
[1,2,3]
2
[1,2]
2
"""
