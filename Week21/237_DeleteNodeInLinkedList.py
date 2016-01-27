#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        if not node:
            return None
        while node.next:
            node.val = node.next.val
            if node.next.next:
                node = node.next
            else:
                node.next = None
                break
