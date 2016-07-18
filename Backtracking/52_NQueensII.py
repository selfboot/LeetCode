#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    countNQueens = 0

    def totalNQueens(self, n):
        self.countNQueens = 0
        cols_used = [-1 for i in range(n)]
        self.solveNQueens(0, cols_used, n)
        return self.countNQueens

    def solveNQueens(self, row, cols_used, n):
        for col in range(n):
            if self.isValid(row, col, cols_used, n):
                if row == n - 1:
                    self.countNQueens += 1
                    return

                cols_used[row] = col
                self.solveNQueens(row + 1, cols_used, n)
                cols_used[row] = -1

    def isValid(self, row, col, cols_used, n):
        """ Can check isvalid with using hash, implemented by c++.

        Refer to:
        https://discuss.leetcode.com/topic/13617/accepted-4ms-c-solution-use-backtracking-and-bitmask-easy-understand
        The number of columns is n, the number of 45° diagonals is 2 * n - 1,
        the number of 135° diagonals is also 2 * n - 1.
        When reach [row, col], the column No. is col,
        the 45° diagonal No. is row + col and the 135° diagonal No. is n - 1 + col - row.

        | | |                / / /             \ \ \
        O O O               O O O               O O O
        | | |              / / / /             \ \ \ \
        O O O               O O O               O O O
        | | |              / / / /             \ \ \ \
        O O O               O O O               O O O
        | | |              / / /                 \ \ \
        3 columns        5 45° diagonals     5 135° diagonals    (when n is 3)
        """
        for i in range(row):
            # Check for the according col above the current row.
            if cols_used[i] == col:
                return False

            # Check from left-top to right-bottom
            if cols_used[i] == col - row + i:
                return False

            # Check from right-top to left-bottom
            if cols_used[i] == col + row - i:
                return False
        return True

"""
1
5
8
"""
