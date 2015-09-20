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
        counter = 1                         # The length of the list
        head_counter = head
        # Get te length of the list
        while head_counter.next:
            counter += 1
            head_counter = head_counter.next

        count_from_head = 1
        head_keep = head
        while head.next:
            # The next node will be removed
            if count_from_head == counter - n:
                head.next = head.next.next
                break
            head = head.next
            count_from_head += 1

        # the node removed is the head.
        if counter == n:
            return head_keep.next

        else:
            return head_keep
