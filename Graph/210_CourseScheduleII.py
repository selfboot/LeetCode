#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


class Solution(object):
    """
    Topological Sort:
    1. Find a "start nodes" which have no incoming edges;
    2. delete the node, update the graph. Then goto 1
    If all the nodes can be deleted, then can finish the course.
    """
    def findOrder(self, numCourses, prerequisites):
        edges_hash = {i: [] for i in range(numCourses)}
        in_degree = [0] * numCourses
        for edge in prerequisites:
            edges_hash[edge[1]].append(edge[0])
            in_degree[edge[0]] += 1

        correct_orders = []
        availables = [i for i, v in enumerate(in_degree) if v == 0]
        while availables:
            course = availables[0]
            correct_orders.append(course)
            del availables[0]
            for co in edges_hash[course]:
                in_degree[co] -= 1
                if in_degree[co] == 0:
                    availables.append(co)
        if not sum(in_degree):
            return correct_orders
        else:
            return []

if __name__ == '__main__':
    sol = Solution()
    print sol.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
    print sol.findOrder(4, [[1, 0], [2, 0], [0, 1], [3, 2]])
