#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        negative = 1
        mark = False
        digit_already = False
        digit_char = "0123456789"
        process_str = ""
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
                process_str += char
                continue

            if char not in digit_char and digit_already:
                break

            if char not in digit_char and not digit_already:
                return 0

        result = 0
        for char in process_str:
            result = result * 10 + ord(char) - ord('0')

        result = result * negative
        if result > 2 ** 31 - 1:
            return 2147483647

        if result < -2 ** 31:
            return -2147483648

        return result
