#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <= 1:
            return "1"

        pre_str = "1"
        for i in range(2, n + 1):
            # Get the ith count-and-say sequence by scan pre_str
            length = len(pre_str)
            current_str = ""
            index = 0

            # Count and say the pre_str
            while index < length:
                char = pre_str[index]
                repeat = 0
                pos = repeat + index + 1
                while pos < length and pre_str[pos] == char:
                    repeat += 1
                    pos = repeat + index + 1

                if repeat:
                    current_str = current_str + str(repeat + 1) + char
                else:
                    current_str = current_str + "1" + char
                index = index + repeat + 1

            pre_str = current_str

        return pre_str
