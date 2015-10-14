#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.solve(0, board)

    def solve(self, cur, board):
        if cur == 81:
            return True
        row, col = cur / 9, cur % 9

        # Recursive: check the next cell
        if board[row][col] != '.':
            return self.solve(cur+1, board)

        # Current cell is '.', put one possible num here and do the recursive
        # If no succeed in this num, just backtracking.
        available_nums = self.getAvailableNums(
                            board,
                            row,
                            col)

        if not available_nums:
            return False

        for val in available_nums:
            row_list = list(board[row])
            row_list[col] = val
            board[row] = ''.join(row_list)
            if self.solve(cur + 1, board):
                return True

        # None of the val in available_nums can be put here.
        # And before backtracking, change the current position to '.'
        row_list[col] = '.'
        board[row] = ''.join(row_list)

        return False

    # Get the available numbers in (row, col)
    def getAvailableNums(self, matrix, row, col):
        used_num = ""
        for row_num in matrix[row]:
            if row_num != ".":
                used_num += row_num
        for col_num in matrix:
            if col_num[col] != ".":
                used_num += col_num[col]
        block_row = row / 3 * 3
        block_col = col / 3 * 3
        for r in range(block_row, 3 + block_row):
            for c in range(block_col, block_col + 3):
                if matrix[r][c] != ".":
                    used_num += matrix[r][c]

        available_nums = ""
        for num in "123456789":
            if num not in used_num:
                available_nums += num

        return available_nums

"""
if __name__ == '__main__':
    sol = Solution()
    sudo = ["..9748...",
            "7........",
            ".2.1.9...",
            "..7...24.",
            ".64.1.59.",
            ".98...3..",
            "...8.3.2.",
            "........6",
            "...2759.."]
    sol.solveSudoku(sudo)
    print sudo
"""
