#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# @Last Modified time: 2016-07-04 15:01:41


class Solution(object):
    """ Magic factor 2 and 3.

    Break the numbers into magic factor only 2 and 3 if number >= 4,
    Then we will get the max product.

    If we break a number N into two factors x, N-x, product is p=x(N-x).
    To get the maximum of p,  x=N/2 when N is even, x=(N-1)/2 when N is odd.
    If x can be break again and the product is bigger than x, then break recursively.

    Now the question is, for a given number N, when to stop break.  It's clearly that:
    (N/2)*(N/2) < N (N is even),     then N < 4,  N = 2
    (N-1)/2 *(N+1)/2 < N (N id odd), then N < 5,  N = 3, N = 1

    Thus, the factors of the perfect product should only be 2 or 3.

    According to:
    https://discuss.leetcode.com/topic/45341/an-simple-explanation-of-the-math-part-and-a-o-n-solution
    """
    def integerBreak(self, n):
        assert(n >= 2)
        if n == 2 or n == 3:
            return n - 1
        three_cnt = n / 3
        two_cnt = (n - three_cnt * 3) / 2

        # We should minus one 3 and add two 2,  number may be 10, 13
        if n - three_cnt * 3 == 1:
            two_cnt = 2
            three_cnt -= 1
        return 3 ** three_cnt * (2 ** two_cnt)

"""
2
7
10
102
"""
