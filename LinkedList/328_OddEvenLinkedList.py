#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        if not head or not head.next:
            return head

        odd = ListNode(0)
        even = ListNode(0)
        pre_head = odd
        pre_mid = even
        odd_even_dict = {0: even, 1: odd}
        count = 0
        while head:
            count += 1
            odd_even_dict[count & 1].next = head
            odd_even_dict[count & 1] = head
            head = head.next

        odd_even_dict[0].next = None
        odd_even_dict[1].next = pre_mid.next
        return pre_head.next

"""
[]
[1]
[1,2]
[1,2,3]
[1,2,3,4,5,6,7,8]
"""
