#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    """ Refer to
    https://leetcode.com/discuss/32115/bit-operation-solution-java

    The idea is very simple:
        1. last bit of (odd number & even number) is 0.
        2. when m != n, there is at least an odd number and an even number,
        so the last bit position result is 0;
        3. when m == n: just return m.

    For example: m = xy, n = xz, m < n, so y < z. Here x, y, z are some bits.
    And x is all the shared bits of the high position.
    y < z, so bitwise AND of all numbers in [xy, xz] is x0...0
    """
    # Recursive
    def rangeBitwiseAnd(self, m, n):
        if m == n:
            return m
        else:
            return self.rangeBitwiseAnd(m >> 1, n >> 1) << 1

    # Iteration
    def rangeBitwiseAnd_1(self, m, n):
        if m == 0:
            return 0
        trans_count = 0
        while m < n:
            m >>= 1
            n >>= 1
            trans_count += 1
        return m << trans_count

    # Another simple solution
    def rangeBitwiseAnd_2(self, m, n):
        while m < n:
            n = n & (n-1)
        return n

"""
0
0
12
12
0
2147483647
"""
