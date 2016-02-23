#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


class Solution(object):
    """
    The basic idea is
    "keep deleting leaves layer-by-layer, until reach the root."

    Specifically, first find all the leaves, then remove them.
    After removing, some nodes will become new leaves. So we can
    continue remove them. Eventually, there is only 1 or 2 nodes
    left. If there is only one node left, it is the root. If there
    are 2 nodes, either of them could be a possible root.
    """
    def findMinHeightTrees(self, n, edges):
        if n == 1:
            return [0]

        adj = [[] for i in xrange(n)]
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        leaves = []
        for i in xrange(n):
            if len(adj[i]) == 1:
                leaves.append(i)

        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for node in leaves:
                adj_node = adj[node][0]
                adj[adj_node].remove(node)
                if len(adj[adj_node]) == 1:
                    new_leaves.append(adj_node)
            leaves = new_leaves

        return leaves

"""
1
[]
2
[0,1]
4
[[1,0],[1,2],[1,3]]
"""
