#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        integer_symbols = [["I", "IV", "V", "IX"],
                           ["X", "XL", "L", "XC"],
                           ["C", "CD", "D", "CM"],
                           ["M"]
                           ]
        roman_str = ""
        counter = 0

        while num != 0:
            single = num % 10

            if single in [1, 2, 3]:
                roman_str = single * integer_symbols[counter][0] + roman_str
            elif single == 4:
                roman_str = integer_symbols[counter][1] + roman_str
            elif single == 5:
                roman_str = integer_symbols[counter][2] + roman_str
            elif single in [6, 7, 8]:
                roman_str = integer_symbols[counter][2] +\
                    (single - 5) * integer_symbols[counter][0] +\
                    roman_str
            elif single == 9:
                roman_str = integer_symbols[counter][3] + roman_str
            else:
                num = num / 10
                counter += 1
                continue
            num = num / 10
            counter += 1

        return roman_str

"""
1
100
3999
"""
