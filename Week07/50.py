#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        abs_half = abs(n) / 2

        if n == 0:
            return 1.00

        elif n > 0:
            result = self.myPow(x, abs_half) ** 2
            if n & 1 == 1:
                result *= x
            return result

        else:
            result = 1 / (self.myPow(x, abs_half) ** 2)
            if abs(n) & 1 == 1:
                result *= 1 / x
            return result
