#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        # Calcluate the abs's decimal and then add the symbol
        negative = 0
        if numerator * denominator < 0:
            negative = 1
        numerator, denominator = abs(numerator), abs(denominator)

        answer = []
        answer.append(str(numerator/denominator))
        remainder = numerator % denominator
        if remainder:
            answer.append(".")
        # Keep the start position of the repeating part
        remainder_start = {}
        while remainder:
            remainder *= 10
            if remainder in remainder_start:
                answer.insert(remainder_start[remainder], "(")
                answer.append(")")
                break
            else:
                remainder_start[remainder] = len(answer)
                answer.append(str(remainder/denominator))
                remainder = remainder % denominator
        if negative:
            answer.insert(0, "-")
            return "".join(answer)
        else:
            return "".join(answer)

"""
1
9
-1
999
2
2
-50
-8
-50
8
"""
