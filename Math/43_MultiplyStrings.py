#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def multiply(self, num1, num2):
        """ Simulation the manual way we do multiplication.

        Start from right to left, perform multiplication on every pair of digits.
        And add them together.

        There is a good graph explanation.  Refer to:
        https://discuss.leetcode.com/topic/30508/easiest-java-solution-with-graph-explanation
        """
        m, n = len(num1), len(num2)
        pos = [0] * (m + n)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                multi = int(num1[i]) * int(num2[j])
                pos_sum = pos[i + j + 1] + multi

                # Update pos[i+j], pos[i+j+1]
                pos[i + j] += pos_sum / 10
                pos[i + j + 1] = pos_sum % 10

        first_not_0 = 0
        while first_not_0 < m + n and pos[first_not_0] == 0:
            first_not_0 += 1

        return "".join(map(str, pos[first_not_0:] or [0]))

"""
"0"
"1"
"123"
"123"
"12121212121212125"
"121232323499999252"
"""
