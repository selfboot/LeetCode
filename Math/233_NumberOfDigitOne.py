#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


class Solution(object):
    # Recursive solution
    def countDigitOne(self, n):
        if n <= 0:
            return 0
        elif n < 10:
            return 1
        else:
            units = n % 10
            tens = n / 10
            count = self.countDigitOne(tens - 1) * 10 + tens
            n /= 10
            while n:
                if n % 10 == 1:
                    count = count + 1 + units
                n = n / 10

            if units >= 1:
                count += 1
            return count

"""
-1
6
12
234545
"""
