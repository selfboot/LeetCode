#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        while not l1 and not l2:
            return None

        merged_list = ListNode(0)
        merged_head = merged_list

        # Scan through l1 and l2, get the smaller one to merged list
        while l1 and l2:
            if l1.val <= l2.val:
                node = ListNode(l1.val)
                l1 = l1.next
            else:
                node = ListNode(l2.val)
                l2 = l2.next
            merged_list.next = node
            merged_list = merged_list.next

        # l2 has gone to the tail already and only need to scan l1
        while l1:
            node = ListNode(l1.val)
            l1 = l1.next
            merged_list.next = node
            merged_list = merged_list.next

        # l1 has gone to the tail already and only need to scan l2
        while l2:
            node = ListNode(l2.val)
            l2 = l2.next
            merged_list.next = node
            merged_list = merged_list.next

        return merged_head.next

"""
[]
[]
[1,4,8,12]
[2,3]
[1,3,5,7,9]
[2,4,6,8,10]
"""
