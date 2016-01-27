#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        slow, fast, new_head = head, head, None
        # Reverse the first half while finding the middle.
        while fast and fast.next:
            fast = fast.next.next
            # Reverse the slow nodes, Pythonic way
            new_head, new_head.next, slow = slow, new_head, slow.next
            """ More general way
            next_node = slow.next
            slow.next = new_head
            new_head = slow
            slow = next_node
            """
        # Midle node is slow or slow.next according to the len of list.
        if fast:
            slow = slow.next

        # Compare the reversed(pre_half) and post half
        while new_head and new_head.val == slow.val:
            new_head, slow = new_head.next, slow.next

        return not new_head

"""
[]
[1]
[1,2,2,1]
[1,2,3,2,1]
[1,2,3,4]
"""
