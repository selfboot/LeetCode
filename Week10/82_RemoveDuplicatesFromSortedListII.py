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
        keep_node = distinct_node = ListNode("guard")
        distinct_node.next = head

        # distinct_node: the node only occur once.
        # dis_next_node: always the node occur after distinct_node
        while distinct_node.next:
            dis_next_node = distinct_node.next
            if dis_next_node.next:
                next_node = dis_next_node.next
                is_duplicate = False

                # Skip the duplicates of dis_next_node.
                while next_node.val == dis_next_node.val:
                    is_duplicate = True
                    if next_node.next:
                        next_node = next_node.next
                    else:
                        next_node = None
                        break
                # Make the new dis_next_node occur after distinct_node.
                if is_duplicate:
                    dis_next_node = next_node
                    distinct_node.next = dis_next_node

                # Find one node without duplicate.
                else:
                    distinct_node.next = dis_next_node
                    distinct_node = distinct_node.next
            # If one node is the last node of the link, then it's distinct.
            else:
                distinct_node.next = dis_next_node
                break

        return keep_node.next

"""
[]
[1]
[3,3,3,3,3]
[1,1,1,2,3,4,4,4,4,5]
"""
