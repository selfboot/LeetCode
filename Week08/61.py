#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        new_head = new_head_keep = ListNode(0)

        # Get the length of ListNode
        head_keep = head
        length = 0
        while head:
            length += 1
            head = head.next
        if not length:
            return head

        k = k % length
        # Get the new head after rotated
        head_save = head_keep
        scan_count = 0
        while scan_count < length - k - 1:
            head_save = head_save.next
            scan_count += 1
        new_head.next = head_save.next
        head_save.next = None

        # Get the last node in the original list
        while new_head.next:
            new_head = new_head.next

        # Get merged with the two list
        new_head.next = head_keep

        return new_head_keep.next

"""
[]
0
[1,2,3,4,5]
0
[1,2,3,4,5]
3
[1,2,3,4,5]
10
[]
2
"""
