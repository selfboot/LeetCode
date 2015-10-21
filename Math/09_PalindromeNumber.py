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

        divide = 1
        while x / divide >= 10:
            divide = divide * 10

        # Compare the highest digit and lowest digit recursively.
        while divide >= 10:
            low_digit = x % 10
            high_digit = x / divide
            if low_digit != high_digit:
                return False

            # Get a new x which delete the highest and lowest digit.
            x = x / 10
            divide = divide / 10
            x = x % divide
            # Update the divide.
            divide = divide / 10

        return True

"""
9
10
-2147483648
32023
320023
98765432123456789
"""
