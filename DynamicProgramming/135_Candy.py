#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def candy(self, ratings):
        candies = [0 for i in ratings]
        candies[0] = 1
        children_nums = len(ratings)

        # Scan from left to right
        for i in range(children_nums - 1):
            if ratings[i + 1] > ratings[i]:
                candies[i + 1] = candies[i] + 1
            else:
                candies[i + 1] = 1

        minimum_candies = 0
        # Scan from right to left
        for i in range(children_nums - 1, 0, -1):
            if ratings[i - 1] > ratings[i]:
                candies[i - 1] = max(candies[i] + 1, candies[i - 1])
            else:
                candies[i - 1] = max(1, candies[i - 1])
            minimum_candies += candies[i]

        return minimum_candies + candies[0]


"""
[0]
[2,2,1]
[3,4,8,6,7]
[4,3,8,6,7]
[1,2,4,4,3]
[1,2,4,4,5]
[4,4,4,4,4]
"""
