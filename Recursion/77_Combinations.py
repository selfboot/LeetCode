#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k > n or not n:
            return []

        combine_list = self.combine_k(1, n, k)
        return combine_list

    def combine_k(self, start, n, k):
        combine_k = []
        # k == 1, just return the list[start, end]
        if k == 1:
            for i in range(start, n+1):
                combine_k.append([i])
            return combine_k

        # k > 1, return every i combines all the k-1 th combine in [i+1, n]
        for i in range(start, n+2-k):
            combine_k_1 = self.combine_k(i+1, n, k-1)
            for combine_1 in combine_k_1:
                combine = [i]
                combine.extend(combine_1)
                combine_k.append(combine)

        return combine_k

"""
5
2
2
3
6
6
"""
