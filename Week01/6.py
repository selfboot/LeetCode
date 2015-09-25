#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        magic_num = numRows - 1
        if magic_num == 0:
            return s

        length = len(s)

        column_sum = length / (2 * magic_num) * magic_num
        if length % (2 * magic_num) != 0:
            column_sum += ((length % (2 * magic_num)) % numRows) + 1

        counter = 1
        row = 1
        column = 1
        result_dict = {}
        result = ""

        for char in s:
            # Go Down
            if ((counter - 1) / magic_num) % 2 == 0:
                result_dict[(row - 1) * column_sum + column] = char
                row = row + 1

            # Go up
            else:
                result_dict[(row - 1) * column_sum + column] = char
                row = row - 1
                column = column + 1
            counter += 1

        for key in sorted(result_dict):
            result += result_dict[key]

        return result
