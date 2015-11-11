#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        keep_node = min_last = ListNode(x-1)
        tail_node = min_last

        while head:
            # Insert the node less than x after the last-min node.
            if head.val < x:
                first_greater_node = min_last.next
                next_node = ListNode(head.val)
                min_last.next = next_node
                min_last = next_node
                min_last.next = first_greater_node

                # There are no nodes greater than or equal to x.
                if tail_node.val < x:
                    tail_node = min_last

            # Move the tail forward when meet a node >= x.
            else:
                next_node = ListNode(head.val)
                tail_node.next = next_node
                tail_node = tail_node.next

            head = head.next

        return keep_node.next

"""
[]
1
[2, 4, 3, 2, 5, 2]
3
[3, 7, 8, -5, 2, 6]
-2
"""
