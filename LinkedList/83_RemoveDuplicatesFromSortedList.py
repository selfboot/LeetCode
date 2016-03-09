#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return []

        start_node = head
        while head.next:
            next_node = head.next
            next_val = next_node.val
            while head.val == next_val:
                if next_node.next:
                    next_node = next_node.next
                    next_val = next_node.val
                # When scan to the tail, next_node should be None
                else:
                    next_node = None
                    break
            # If there is no next_node, change the link and break
            if not next_node:
                head.next = None
                break

            # Find the no duplicate next node, move head to it.
            head.next = next_node
            head = head.next

        return start_node

"""
[]
[1]
[3,3,3,3,3]
[1,1,1,2,3,4,4,4,4,5]
"""
