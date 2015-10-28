#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        len_a = len(a)
        len_b = len(b)
        len_min = min(len_a, len_b)

        # Add the common length part
        carry_in = 0
        sum_str = ""
        for index in range(len_min):
            num_a = int(a[len_a - 1 - index])
            num_b = int(b[len_b - 1 - index])
            sum_a_b = (num_a + num_b + carry_in) % 2
            sum_str = str(sum_a_b) + sum_str
            carry_in = (num_a + num_b + carry_in) / 2

        # Add the longer part
        if len_a > len_min:
            num_new = a[:len_a - len_min]
        else:
            num_new = b[:len_b - len_min]
        len_new = len(num_new)
        for i in range(len_new):
            num = int(num_new[len_new - 1 - i])
            sum_num = (num + carry_in) % 2
            sum_str = str(sum_num) + sum_str
            carry_in = (num + carry_in) % 2

        if carry_in:
            sum_str = "1" + sum_str

        return sum_str

"""
"0"
"0"
"111000"
"111111111"
"""
