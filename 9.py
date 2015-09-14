#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        x_keep = x
        result = 0
        while x / 10 != 0:
            result = (result + x % 10) * 10
            x = x / 10

        result += x % 10
        if result - x_keep == 0:
            return True
        else:
            return False
