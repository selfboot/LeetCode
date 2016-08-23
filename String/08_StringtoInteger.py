#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    MAX_INT = 2**31 - 1
    MIN_INT = - 2**31

    def myAtoi(self, strs):
        """ We need to handle four cases:

        1. discards all leading whitespaces
        2. sign of the number
        3. overflow
        4. invalid input
        """
        strs = strs.strip()
        if not strs:
            return 0

        sign, i = 1, 0
        if strs[i] == '+':
            i += 1
        elif strs[i] == '-':
            i += 1
            sign = -1

        num = 0
        while i < len(strs):
            if strs[i] < '0' or strs[i] > '9':
                break
            if num > self.MAX_INT or (num * 10 + int(strs[i]) > self.MAX_INT):
                return self.MAX_INT if sign == 1 else self.MIN_INT
            else:
                num = num * 10 + int(strs[i])
            i += 1

        return num * sign

"""
""
"  12a"
"  a12"
"  +12"
"  +-12"
"2147483648"
"-2147483648"
"""
