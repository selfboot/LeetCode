#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def trailingZeroes(self, n):
        if n < 5:
            return 0

        sums = 0
        i = 1
        # Every five numbers will produce a trailing 0
        # when meet 25, 125, 625, ..., it will get addtional 0.
        while n / (5*i) >= 1:
            sums += n / (5*i)
            i *= 5
        return sums

"""
0
5
7
10
25
"""
