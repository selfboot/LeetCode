#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return []

        head = merged_list = ListNode(0)
        heap_record = []
        # push head of all the linked list to heap
        for node in lists:
            if node:
                heap_record.append((node.val, node))
        heapq.heapify(heap_record)

        # get the min val and push the node into heap
        while heap_record:
            min_node = heapq.heappop(heap_record)
            merged_list.next = min_node[1]
            merged_list = merged_list.next
            if min_node[1].next:
                next_node = min_node[1].next
                heapq.heappush(heap_record, (next_node.val, next_node))

        return head.next

"""
[]
[[1,4,5,6,9], [2,3,4,5,6,8], [0,1,2,3,4], [2,2,2,2]]
"""
