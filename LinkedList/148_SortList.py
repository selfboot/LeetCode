#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # Merge Sort
    def sortList(self, head):
        if not head or not head.next:
            return head
        # Get the two half parts.
        pre_slow = None
        slow = fast = head
        while fast and fast.next:
            pre_slow = slow
            slow = slow.next
            fast = fast.next.next
        pre_slow.next = None        # Cut the linked list to two parts.
        left_list = self.sortList(head)
        right_list = self.sortList(slow)
        return self.merge(left_list, right_list)

    # Operator merge.
    def merge(self, left_list, right_list):
        pre_head = dummy = ListNode(0)
        while left_list and right_list:
            if left_list.val < right_list.val:
                dummy.next = left_list
                left_list = left_list.next
            else:
                dummy.next = right_list
                right_list = right_list.next
            dummy = dummy.next

        if left_list:
            dummy.next = left_list
        if right_list:
            dummy.next = right_list

        return pre_head.next
"""
[]
[1]
[1,2]
[5,1,2]
[5,1,2,3]
"""
