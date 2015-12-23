#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reorderList(self, head):
        """
        Firstly, use two pointer to find the mid node_keep,
        Then reverse the post half nodes, and merge the pre half and
        post reversed half.
        """
        if not head or not head.next or not head.next.next:
            return
        slow = fast = head
        while fast.next:
            if fast.next.next:
                slow = slow.next
                fast = fast.next.next
            else:
                break

        post_half_start = slow.next
        slow.next = None
        reverse_head = self.reverse_list(post_half_start)
        while head and reverse_head:
            node_keep = head.next
            reverse_node_keep = reverse_head.next
            head.next = reverse_head
            reverse_head.next = node_keep
            head = node_keep
            reverse_head = reverse_node_keep

    # Reverse a linked list
    def reverse_list(self, head):
        pre_node = None
        post_node = None
        while head:
            post_node = head.next
            head.next = pre_node
            pre_node = head
            head = post_node

        return pre_node

    # RuntimeError: maximum recursion depth exceeded
    """
    def reverse_list(self, head):
        if not head.next:
            return head
        next_node = head.next
        new_head = self.reverse_list(next_node)
        next_node.next = head
        head.next = None
        return new_head
    """

"""
[]
[1]
[1,2]
[1,2,3,4,5,6]
[1,2,3,4,5]
"""
