#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry_in = 0
        head = ListNode(0)
        l_sum = head

        while l1 and l2:
            l_sum.next = ListNode((l1.val + l2.val + carry_in) % 10)
            carry_in = (l1.val + l2.val + carry_in) / 10
            l1 = l1.next
            l2 = l2.next
            l_sum = l_sum.next

        if l1:
            while l1:
                l_sum.next = ListNode((l1.val + carry_in) % 10)
                carry_in = (l1.val + carry_in) / 10
                l1 = l1.next
                l_sum = l_sum.next

        if l2:
            while l2:
                l_sum.next = ListNode((l2.val + carry_in) % 10)
                carry_in = (l2.val + carry_in) / 10
                l2 = l2.next
                l_sum = l_sum.next

        if carry_in != 0:
            l_sum.next = ListNode(carry_in)

        return head.next
