#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return [1]

        carry_in = (digits[-1] + 1)/10
        digits[-1] = (digits[-1] + 1) % 10

        index = len(digits) - 2
        # Every position is the sum of post position and carry_in mod 10
        while index >= 0:
            if digits[index] + carry_in == 10:
                digits[index] = 0
                carry_in = 1
                index -= 1
            else:
                digits[index] += carry_in
                carry_in = 0
                break

        # Add the pre carry in number.
        if carry_in and index == -1:
            digits.insert(0, 1)

        return digits

"""
[0]
[1,2,3,4,5,6]
[9,9,9,9,9,9]
"""
