#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    # pythonic
    def hammingWeight(self, n):
        bit_list = list('{0:032b}'.format(n))
        count = 0
        for bit in bit_list:
            count += int(bit)
        return count

    # Bit manipulation
    def hammingWeight_1(self, n):
        count = 0
        for i in range(32):
            count += (n >> i) & 1
        return count

"""
if __name__ == '__main__':
    sol = Solution()
    print sol.hammingWeight(11)
    print sol.hammingWeight_1(11)
"""
