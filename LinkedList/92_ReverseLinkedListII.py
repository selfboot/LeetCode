#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        reverse_count = 1
        reverse_start_node = ListNode(0)
        reverse_start_node.next = head
        keep_node = reverse_start_node
        while reverse_count < n:
            # Get the node(reverse_start_node) before the reversed position.
            if reverse_count < m:
                reverse_start_node = head
                head = head.next
                reverse_count += 1
            # Insert the node after current head to the reversed position.
            else:
                assert(head.next)
                be_reversed_node = head.next

                # Build the connection in the reversed list's tail.
                tail_next_node = be_reversed_node.next
                head.next = tail_next_node

                # Build the connection in the reversed list's head.
                head_next_node = reverse_start_node.next
                reverse_start_node.next = be_reversed_node
                be_reversed_node.next = head_next_node

                reverse_count += 1

        return keep_node.next

"""
[1]
1
1
[1,2,3,4,5,6,7]
1
7
"""
