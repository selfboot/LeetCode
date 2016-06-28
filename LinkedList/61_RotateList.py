#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """No benefit by using slow/fast pointers to find the tail node.

        So just find the total length, and then do the rotate.
        """
        # Get the length of ListNode
        if not head or not head.next:
            return head

        len_scan, length = head, 0
        while len_scan:
            length += 1
            len_scan = len_scan.next

        # Get the new head after rotated
        k = k % length
        if not k:
            return head
        scan_count = 0
        new_tail = head
        while scan_count < length - k - 1:
            new_tail = new_tail.next
            scan_count += 1

        new_head = new_tail.next
        # Set the rotated right part point to none.
        new_tail.next = None

        # Get the last node in the original list
        original_tail = new_head
        while original_tail and original_tail.next:
            original_tail = original_tail.next

        # Merge the two list
        original_tail.next = head

        return new_head

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
