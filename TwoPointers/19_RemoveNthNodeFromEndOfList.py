#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        steps = 0
        first = head
        # Let the first pointer goto n+1'th node.
        while first:
            first = first.next
            steps += 1
            if steps == n + 1:
                break

        # the node to be removed is the head node.
        if steps < n + 1:
            return head.next

        # Let second move with first one by one. When first meet the NULL
        # Second will meet the (N+1)th Node from end of list.
        second = head
        while first:
            first = first.next
            second = second.next

        # Next node of the second will be removed.
        second.next = second.next.next
        return head

"""
[1]
1
[1,2,3,4,5,6,7,8]
5
[1,2,3,4,5,6,7,8]
8
"""
