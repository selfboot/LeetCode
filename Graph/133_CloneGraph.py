#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return None

        copyed_node_pair = {}
        copy_head = UndirectedGraphNode(node.label)
        copy_head.neighbors = []
        copyed_node_pair[node] = copy_head

        nodes_stack = []
        nodes_stack.append(node)
        while nodes_stack:
            one_node = nodes_stack.pop()

            for neighbor in one_node.neighbors:
                if neighbor not in copyed_node_pair:
                    copy_node = UndirectedGraphNode(neighbor.label)
                    copy_node.neighbors = []
                    copyed_node_pair[neighbor] = copy_node
                    nodes_stack.append(neighbor)

                copyed_node_pair[one_node].neighbors.append(
                    copyed_node_pair[neighbor])

        return copy_head

"""
{0,0,0}
{0,1,2#1,2#2,2}
"""
