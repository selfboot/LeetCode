#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# @Last Modified time: 2016-04-05 16:17:53

"""
According to: https://leetcode.com/discuss/88153/another-python

Draw a line of length a. Then draw further lines of lengths b, c, etc.
How does the a-line get crossed?
From the left by the d-line or from the right by the f-line.

           b                              b
   +----------------+             +----------------+
   |                |             |                |
   |                |             |                | a
 c |                |           c |                |
   |                | a           |                |    f
   +------------------>           |             <---------+
            d       |             |                |      | e
                    |             |                       |
                                  +-----------------------+
                                              d
The "special case" of the e-line stabbing the a-line from below.

"""


class Solution(object):
    def isSelfCrossing(self, x):
        if not x or len(x) < 4:
            return False
        b = c = d = e = f = 0  # Initinal
        for a in x:
            if d >= b > 0 and (a >= c > 0 or (a >= c-e >= 0 and f >= d-b)):
                return True
            b, c, d, e, f = a, b, c, d, e
        return False

"""
[]
[2,2]
[1,1,1,1]
[6,4,3,2,2,1,5]
[1,1,2,2,3,3,4,4]
"""
