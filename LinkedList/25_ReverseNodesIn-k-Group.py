#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if not head or k <= 1:
            return head

        solution = ListNode(0)
        solution.next = head
        before_node = solution
        count = 0

        # Get each k nodes and reverse all of them
        while head:
            count += 1
            if count % k == 0:
                after_node = head.next
                before_node = self.reverse_k_nodes(before_node, after_node)
                head = after_node
            else:
                head = head.next

        return solution.next

    def reverse_k_nodes(self, before_node, after_node):
        """
        Given a situation    : ... -> B -> | C -> ... -> X | -> Y -> ...
        Nodes before C is swaped, and then we should swap node between C and X,
        so the result is     : ... -> B -> | X -> ... -> C | -> Y -> ...
        Then what we need to is:
            1. Get node C and make it as tail in k-reversed-list:  C
            2. Get all the other nodes and put each before the
               head of current k-reversed-list:  X -> ... ->C
            3. Make B.next = X and C.next = Y:
                -> B -> | X -> ... -> C  | -> Y
        """
        if before_node.next == after_node:
            pass

        # Step 2
        head = before_node.next
        reversed_list_head = reversed_list_tail = head
        cur_node = head.next
        while cur_node != after_node:
            keep_node = cur_node.next
            cur_node.next = reversed_list_head
            reversed_list_head = cur_node
            cur_node = keep_node

        # Step 3
        before_node.next = reversed_list_head
        reversed_list_tail.next = after_node
        return reversed_list_tail

"""
[]
1
[1]
1
[1,2,3,4,5,6,7,8,9]
4
"""
