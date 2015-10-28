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
        while index >= 0:
            if digits[index] + carry_in == 10:
                digits[index] = 0
                carry_in = 1
                index -= 1
            else:
                digits[index] += carry_in
                carry_in = 0
                break

        if carry_in and index == -1:
            temp = [1]
            temp.extend(digits)
            digits = temp

        return digits
