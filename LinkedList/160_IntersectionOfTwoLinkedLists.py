#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        # Refer to:
        # https://leetcode.com/discuss/17278/accepted-shortest-explaining-algorithm-comments-improvements
        p1, p2 = headA, headB
        while(p1 != p2):
            p1 = headB if not p1 else p1.next
            p2 = headA if not p2 else p2.next
        return p1
