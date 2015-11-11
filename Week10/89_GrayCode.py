#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if not n:
            return [0]

        if n == 1:
            return [0, 1]

        # Consume n's sequence is: 0..0, 0..1, ..., 1..0
        # When comes to n+1, it's sequence is simple as followers:
        # 0{0..0, 0..1, ..., 1..0}, 1{1..0, ..., 0..1, 0..0}
        # Then second part of past line is just a reverse of n's sequence.
        high_digit = 2 ** (n-1)
        gray_code_list = self.grayCode(n-1)
        for num in gray_code_list[::-1]:
            gray_code_list.append(high_digit + num)

        return gray_code_list

"""
0
2
3
4
"""
