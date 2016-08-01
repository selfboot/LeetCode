#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


class Solution(object):
    def findItinerary(self, tickets):
        """ Eulerian path. Hierholzer Algorithm, greedy DFS with backtracking.

        Refer to: Short Ruby / Python / Java / C++
        https://discuss.leetcode.com/topic/36370/short-ruby-python-java-c
        """
        import collections
        targets = collections.defaultdict(list)
        for a, b in sorted(tickets, reverse=True):
            targets[a] += b,
        route = []

        def visit(airport):
            while targets[airport]:
                visit(targets[airport].pop())
            route.append(airport)
        visit('JFK')

        return route[::-1]

"""
[["JFK", "MUC"], ["JFK", "SJC"], ["SJC", "JFK"], ["MUC", "ATL"]]
[["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
[["JFK", "MUC"], ["MUC", "SJC"], ["SJC", "ATL"], ["MUC", "LHR"], ["LHR", "SJC"]]
"""
