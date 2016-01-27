#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
from collections import deque


class Solution(object):
    # Implemented in array, slower than deque
    def maxSlidingWindow(self, nums, k):
        max_num = []
        queue = []
        for i, v in enumerate(nums):
            # remove numbers out of range k
            if queue and queue[0] == i-k:
                queue = queue[1:]
            # remove smaller numbers in k range as they are useless
            while queue and v > nums[queue[-1]]:
                queue.pop()
            queue.append(i)
            if i+1 >= k:
                max_num.append(nums[queue[0]])

        return max_num


class Solution_2(object):
    # Implemented in dqueue, much faster
    def maxSlidingWindow(self, nums, k):
        max_num = []
        queue = deque()
        for i, v in enumerate(nums):
            if queue and queue[0] == i-k:
                queue.popleft()
            while queue and v > nums[queue[-1]]:
                queue.pop()
            queue.append(i)
            if i+1 >= k:
                max_num.append(nums[queue[0]])

        return max_num
"""
[]
0
[1,3,-1,-3,5,3,6,7]
3
[1,3,-1,-3,5,3,6,7]
2
"""
