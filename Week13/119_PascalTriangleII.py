#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        rowIndex += 1
        row_nums = [0 for i in range(rowIndex)]
        row_nums[0] = 1
        # Use the post part of pre row to update the current row.
        for i in range(1, rowIndex):
            symmetry_count = (i+1)/2    # The symmetry element's numbers
            for j in range(symmetry_count):
                num = row_nums[i-1-j]
                if i > j-1 >= 0:
                    num += row_nums[i-j]
                row_nums[j] = num
            # Get the mid num in odd rows
            if (i+1) % 2 != 0:
                row_nums[symmetry_count] = 2 * row_nums[i/2]
                symmetry_count += 1
            # Update the post (symmetry) part of current row
            for k in range(symmetry_count, i+1):
                row_nums[k] = row_nums[i-k]
        return row_nums

"""
0
3
8
"""
