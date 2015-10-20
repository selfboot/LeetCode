#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = 1
        if x < 0:
            negative = -1
            x = x * -1

        result = 0
        while x / 10 != 0:
            result = (result + x % 10) * 10
            x = x / 10
        result += x % 10

        if abs(result) > 2 ** 31 - 1:
            return 0
        return result * negative
