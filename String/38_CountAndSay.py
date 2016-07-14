#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    """ Quite straight-forward solution.

    We generate k-th string, and from k-th string we generate k+1-th string,
    until we generate n-th string.
    """
    def countAndSay(self, n):
        if n <= 1:
            return "1"

        pre_str = "1"
        for i in range(2, n + 1):
            # Get the ith count-and-say sequence by scan pre_str
            length = len(pre_str)
            current_str = ""

            # Count and say the pre_str
            index = 0
            while index < length:
                char = pre_str[index]
                repeat = 0
                pos = index + 1
                while pos < length and pre_str[pos] == char:
                    repeat += 1
                    pos += 1

                current_str += str(repeat + 1) + char
                index = pos

            pre_str = current_str

        return pre_str

"""
1
5
15
"""
