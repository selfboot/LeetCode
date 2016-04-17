#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # recursively reverse
    def reverseList(self, head):
        if not head or not head.next:
            return head
        reverse_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return reverse_head

    # iteratively reverse
    def reverseList_2(self, head):
        reverse_head = None
        while head:
            next_node = head.next
            head.next = reverse_head
            reverse_head = head
            head = next_node
        return reverse_head

"""
[]
[1]
[1,2]
[1,2,3,4,5]
"""
