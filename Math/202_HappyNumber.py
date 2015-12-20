#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def isHappy(self, n):
        square_sum = 0
        sum_record = {}
        while n:
            square_sum += (n % 10) ** 2
            n = n / 10

            if not n:
                if square_sum == 1:
                    return True
                if square_sum in sum_record:
                    return False
                else:
                    n = square_sum
                    square_sum = 0
                    sum_record[n] = 1

"""
1
19
20
"""
