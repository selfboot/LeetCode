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
    def canFinish(self, numCourses, prerequisites):
        course_req_dict = {}
        # pre_count: the num of one node's incoming edges.
        pre_count = [0] * numCourses
        for edge in prerequisites:
            if edge[1] not in course_req_dict:
                course_req_dict[edge[1]] = [edge[0]]
            else:
                course_req_dict[edge[1]].append(edge[0])
            pre_count[edge[0]] += 1

        # Keep nodes which have no incoming edges.
        available = [i for i, v in enumerate(pre_count) if v == 0]
        while available:
            course = available[0]
            del available[0]

            for post_course in course_req_dict.get(course, []):
                pre_count[post_course] -= 1
                if pre_count[post_course] == 0:
                    available.append(post_course)
        return sum(pre_count) == 0

"""
1
[]
10
[[1,2],[3,4],[4,5],[5,6],[5,8],[5,9]]
10
[[1,2],[3,4],[4,5],[5,6],[5,8],[6,4]]
"""
