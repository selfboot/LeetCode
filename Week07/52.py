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
if __name__ == '__main__':
    sol = Solution()
    print sol.totalNQueens(8)
"""
