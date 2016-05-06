#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        reversed_x = 0
        original_x = x
        while x > 0:
            reversed_x = reversed_x * 10 + x % 10
            x /= 10
        return reversed_x == original_x


# Pythonic way.
class Solution_2(object):
    def isPalindrome(self, x):
        return x >= 0 and str(x) == str(x)[::-1]


"""
9
10
-2147483648
32023
320023
98765432123456789
"""
