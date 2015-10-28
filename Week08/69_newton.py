#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if not x:
            return x
        val = x
        sqrt_x = (val + x * 1.0 / val) / 2.0
        # Newton iterative method
        while val - sqrt_x > 0.001:
            val = sqrt_x
            sqrt_x = (val + x * 1.0 / val) / 2.0

        return int(sqrt_x)
