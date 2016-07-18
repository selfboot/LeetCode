#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    allNQueens = []

    def solveNQueens(self, n):
        self.allNQueens = []
        self.cols = [True] * n
        self.left_right = [True] * (2 * n - 1)
        self.right_left = [True] * (2 * n - 1)
        queueMatrix = [["."] * n for row in range(n)]
        self.solve(0, queueMatrix, n)

        return self.allNQueens

    def solve(self, row, matrix, n):
        """
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

        # Get one Queen Square
        if row == n:
            result = ["".join(r) for r in matrix]
            self.allNQueens.append(result)
            return

        for col in range(n):
            if self.cols[col] and self.left_right[row + n - 1 - col] and self.right_left[row + col]:
                matrix[row][col] = "Q"
                self.cols[col] = self.left_right[row + n - 1 - col] = self.right_left[row + col] = False
                # Solve the child question
                self.solve(row + 1, matrix, n)
                # Backtracking here.
                matrix[row][col] = "."
                self.cols[col] = self.left_right[
                    row + n - 1 - col] = self.right_left[row + col] = True

"""
1
5
8
"""
