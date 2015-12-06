#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None

        # Get the two list's length
        len_a, len_b = 0, 0
        node_a, node_b = headA, headB
        while node_a:
            len_a += 1
            node_a = node_a.next
        while node_b:
            len_b += 1
            node_b = node_b.next

        # Skip the long list's extra node.
        long_list = headA if len_a >= len_b else headB
        short_list = headB if len_a >= len_b else headA
        for i in range(abs(len_a-len_b)):
            long_list = long_list.next

        # Scan the possible intersection node.
        while short_list:
            if short_list == long_list:
                return short_list
            else:
                short_list = short_list.next
                long_list = long_list.next
        return None
"""
# Refer to:
# https://leetcode.com/discuss/61721/python-solution-o-n-time-and-o-1-space
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None

        tail_a = headA
        while tail_a.next:
            tail_a = tail_a.next
        tail_a.next = headA

        slow = headB
        fast = headB
        is_intersect = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                is_intersect = True
                break
        if not is_intersect:
            tail_a.next = None
            return None

        cur_node_b = headB
        while cur_node_b != slow:
            cur_node_b = cur_node_b.next
            slow = slow.next

        tail_a.next = None
        return cur_node_b
"""
