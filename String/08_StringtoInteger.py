#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        negative = 1
        mark = False                # Mark if has a '+' or '-'
        digit_already = False       # Record if has numerical digits already.
        digit_char = "0123456789"
        result = 0
        for char in str:
            if char == " " and not mark and not digit_already:
                continue

            if char == "-" and not mark:
                negative = -1
                mark = True
                continue

            if char == "+" and not mark:
                mark = True
                continue

            if char in digit_char:
                digit_already = True
                result = result * 10 + ord(char) - ord('0')
                continue

            if char not in digit_char and digit_already:
                break

            if char not in digit_char and not digit_already:
                return 0

        result = result * negative
        if result > 2 ** 31 - 1:
            return 2147483647

        if result < -2 ** 31:
            return -2147483648

        return result

"""
""
"  12a"
"  a12"
"""
