#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    allNQueens = []

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.allNQueens = []
        queueMatrix = [["." for col in range(n)] for row in range(n)]
        self.solve(0, queueMatrix, n)

        return self.allNQueens

    def solve(self, row, matrix, n):
        for col in range(n):
            if self.isValid(row, col, matrix, n):
                matrix[row][col] = "Q"

                # Get one Queen Square
                if row == n - 1:
                    result = []
                    for i in range(n):
                        row_str = "".join(matrix[i])
                        result.append(row_str)
                    self.allNQueens.append(result)
                    matrix[row][col] = "."
                    return

                # Solve the child question
                self.solve(row + 1, matrix, n)
                matrix[row][col] = "."

    def isValid(self, row, col, matrix, n):
        # Check for the according col above the current row.
        for i in range(row):
            if matrix[i][col] == "Q":
                return False

        # Check from left-top to right-bottom
        step_1 = 1
        while row - step_1 >= 0 and col - step_1 >= 0:
            if matrix[row - step_1][col - step_1] == "Q":
                return False
            step_1 += 1

        # Check from right-top to left-bottom
        step_2 = 1
        while row - step_2 >= 0 and col + step_2 < n:
            if matrix[row - step_2][col + step_2] == "Q":
                return False
            step_2 += 1

        return True

"""
if __name__ == '__main__':
    sol = Solution()
    print sol.solveNQueens(2)
"""
