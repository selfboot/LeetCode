#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return -1

        negative = -1     # Make sure it's positive or negative
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            negative = negative * -1
        dividend = abs(dividend)
        divisor = abs(divisor)

        answer = 0

        while dividend >= divisor:
            multi_power = 0
            multi_divisor = divisor

            # Get the biggest n which dividend - divisor * 2^n >= 0
            while dividend >= multi_divisor:
                multi_power += 1
                multi_divisor = multi_divisor << 1
            dividend = dividend - (multi_divisor >> 1)
            answer += 1 << (multi_power - 1)

        if (answer * negative > 2 ** 31 - 1) or (answer * negative < - 2 ** 31):
            return 2 ** 31 - 1
        return answer * negative
