#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[list[str]]
        :rtype: int
        """

        if not matrix:
            return 0

        m_rows = len(matrix)
        n_cols = len(matrix[0])

        # Pre-process: to make every row be a histogram
        process_matrix = [
            [0 for col in range(n_cols)] for row in range(m_rows)]
        for row in range(m_rows):
            for col in range(n_cols):
                if row == 0:
                    if matrix[row][col] == "1":
                        process_matrix[row][col] = 1

                else:
                    num = 1 if matrix[row][col] == "1" else 0
                    process_matrix[row][col] = num * (
                        num + process_matrix[row-1][col])

        # Find every max size of row.
        max_size = 0
        for row in range(m_rows):
            max_row_size = self.largestRectangleArea(process_matrix[row])
            max_size = max(max_row_size, max_size)
        return max_size

    # Find the largest rectangle in a histogram
    def largestRectangleArea(self, height):
        # Add a bar of height 0 after the tail.
        height.append(0)
        size = len(height)
        no_decrease_stack = [0]
        max_size = height[0]

        i = 0
        while i < size:
            cur_num = height[i]
            # If the height of current bar is higher than the stack top,
            # or the stack is empty, push current index to stack
            if (not no_decrease_stack or
                    cur_num > height[no_decrease_stack[-1]]):
                no_decrease_stack.append(i)
                i += 1

            # The current height is lower or same than the top,
            # then pop until current height is higher than the top.
            else:
                index = no_decrease_stack.pop()
                if no_decrease_stack:
                    width = i - no_decrease_stack[-1] - 1
                else:
                    width = i
                max_size = max(max_size, width * height[index])

        return max_size

"""
[]
[["1","0","1","0"], ["1","1","1","1"]]
"""
