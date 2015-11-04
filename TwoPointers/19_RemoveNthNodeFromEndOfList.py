#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        ptr_1 = 1
        head_ptr = head
        # Let the first pointer goto n'th node.
        while ptr_1 < n:
            ptr_1 += 1
            head_ptr = head_ptr.next

        # the node to be removed is the head node.
        if not head_ptr.next:
            return head.next

        # When head_ptr move 1 step, head just move 1 step too.
        # And we use pre_node to remember the pre-node of current head.
        pre_node = head_keep = head
        while head_ptr.next:
            pre_node = head
            head = head.next
            head_ptr = head_ptr.next

        # Next node of the pre_node will be removed.
        pre_node.next = pre_node.next.next
        return head_keep

"""
[1]
1
[1,2,3,4,5,6,7,8]
5
[1,2,3,4,5,6,7,8]
8
"""
