#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbols_integer = {"I": 1, "V": 5, "X": 10, "L": 50,
                           "C": 100, "D": 500, "M": 1000,
                           "IV": 4, "IX": 9, "XL": 40, "XC": 90,
                           "CD": 400, "CM": 900
                           }
        length = len(s)
        integer = 0
        isPass = False
        for i in range(length):
            # Subtractive notation use this symbol
            if isPass:
                isPass = False
                continue
            # Just add the integer
            if s[i] in symbols_integer and s[i:i + 2] not in symbols_integer:
                integer = integer + symbols_integer[s[i]]
                isPass = False
                continue

            # Subtractive notation is used as follows.
            if s[i:i + 2] in symbols_integer:
                integer = integer + symbols_integer[s[i:i + 2]]
                isPass = True

        return integer

"""
"DCXXI"
"CDCM"
"""
