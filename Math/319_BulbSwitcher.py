#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


class Solution(object):
    def bulbSwitch(self, n):
        """
        A bulb ends up on iff it is switched an odd number of times.
        Call them bulb 1 to bulb n.
        Bulb i is switched in round d if and only if d divides i.
        So bulb i ends up on if and only if it has an odd number of divisors.
        """
        return int(n ** 0.5)
        """
        count = 0
        for i in xrange(1, n+1):
            if i * i < (n+1):
                count += 1
            else:
                break
        return count
        """
"""
0
1
2
3
4
12
1908
"""
