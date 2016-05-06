#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Refer to: https://leetcode.com/discuss/27405/o-1-bit-operation-c-solution-8ms


class Solution(object):
    # Pythonic way, easy to understand.
    def reverseBits(self, n):
        bit_str = '{0:032b}'.format(n)
        reverse_str = bit_str[::-1]
        return int(reverse_str, 2)

    # General way, easy to understand.
    def reverseBits_1(self, n):
        reversed = 0
        for i in range(32):
            reversed = reversed << 1
            reversed |= (n >> i) & 0x1
        return reversed

    """
    Divide and Conquer!  Someway like merge sort.
    For example, if there are 8 bit binary number abcdefgh,
    the process is as follow:
    abcdefgh -> efghabcd -> ghefcdab -> hgfedcba
    """
    def reverseBits_2(self, n):
        # For python, there is no 32bit int, so we need to force it 32 bits.
        n = (n >> 16) | (n << 16) & 0xffffffff
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8) & 0xffffffff
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4) & 0xffffffff
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2) & 0xffffffff
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1) & 0xffffffff
        return n

'''
if __name__ == '__main__':
    sol = Solution()
    print sol.reverseBits(43261596)
    print sol.reverseBits_2(43261596)
'''
