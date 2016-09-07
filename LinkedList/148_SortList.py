#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# @Last Modified time: 2016-09-06 20:03:53


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Merge Sort
class Solution(object):
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
        pre_head = dummy = ListNode(None)
        while left_list and right_list:
            if left_list.val < right_list.val:
                dummy.next = left_list
                left_list = left_list.next
            else:
                dummy.next = right_list
                right_list = right_list.next
            dummy = dummy.next

        dummy.next = left_list or right_list

        return pre_head.next


# Quick sort:  Time Limit Exceeded
class Solution_2(object):
    def partition(self, begin, end):
        if not begin or begin.next == end:
            return begin
        pivot = begin.val
        keep, pos = begin, begin
        scan = begin.next
        while scan != end:
            if scan.val <= pivot:
                pos = pos.next
                if scan != pos:
                    scan.val, pos.val = pos.val, scan.val
            scan = scan.next

        pos.val, keep.val = keep.val, pos.val
        return pos

    def quick_sort(self, begin, end):
        if begin == end or begin.next == end:
            return begin

        pos = self.partition(begin, end)
        head = self.quick_sort(begin, pos)
        self.quick_sort(pos.next, end)
        return head

    def sortList(self, head):
        return self.quick_sort(head, None)

"""
[]
[1]
[1,2]
[5,1,2]
[5,1,2,3]
[5,1,2,3,6,7,8,9,12,2]
"""
