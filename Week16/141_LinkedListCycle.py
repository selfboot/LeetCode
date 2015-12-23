#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Refer to http://www.cnblogs.com/hiddenfox/p/3408931.html


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    """
    Two pointers: one go 1 step, another one go 2 steps every time.
    Then if the list has a cycle, fast one will meet the slow one absolutely.
    Prove as follows:
    1. If has a circle
        Assume there are m nodes that not in cycle, and then k nodes in cycle.
        And slow one now go m+i nodes, fast one go 2m + 2i nodes whitout doubt.
        So, slow one in the i's node of the circle, and fast one m+2i
        That's say, fast one goes m+i steps more than slow one.
        As the nodes keep going,
        i grows so (m+i) mode k == 0, then fast and slow meet here.
    2. If not:
        fast one will meet None node.
    """
    def hasCycle(self, head):
        if not head:
            return False
        one_step = head
        two_steps = head
        while two_steps and two_steps.next:
            one_step = one_step.next
            two_steps = two_steps.next.next
            if two_steps and one_step == two_steps:
                return True
        return False
