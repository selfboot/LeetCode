#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Recursive way.
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        merged_head = None
        if(l1.val <= l2.val):
            merged_head = l1
            merged_head.next = self.mergeTwoLists(l1.next, l2)
        else:
            merged_head = l2
            merged_head.next = self.mergeTwoLists(l1, l2.next)
        return merged_head


# Iteratively
class Solution_2(object):
    def mergeTwoLists(self, l1, l2):
        merged_list = ListNode(0)
        merged_head = merged_list

        # Scan through l1 and l2, get the smaller one to merged list
        while l1 and l2:
            if l1.val <= l2.val:
                merged_list.next = l1
                l1 = l1.next

            else:
                merged_list.next = l2
                l2 = l2.next
            merged_list = merged_list.next

        # l2 has gone to the tail already and only need to scan l1
        while l1:
            merged_list.next = l1
            l1 = l1.next
            merged_list = merged_list.next

        # l1 has gone to the tail already and only need to scan l2
        while l2:
            merged_list.next = l2
            l2 = l2.next
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
