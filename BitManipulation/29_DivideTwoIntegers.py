#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    # According to:
    # https://leetcode.com/discuss/38997/detailed-explained-8ms-c-solution
    # Key concept:
    # division simply requires us to find how many times we can subtract the
    # divisor from the the dividend without making the dividend negative.

    def divide(self, dividend, divisor):
        if divisor == 0:
            return -1

        # Make sure it's positive or negative
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        answer = 0

        while dividend >= divisor:
            multiple, temp = 1, divisor
            while dividend >= (temp << 1):
                multiple <<= 1
                temp <<= 1
            dividend -= temp
            answer += multiple

        if not positive:
            answer = -answer

        if (answer > 2147483647) or (answer < -2147483648):
            return 2147483647
        return answer

"""
0
1
12
3
125
-4
1
-1
"""
