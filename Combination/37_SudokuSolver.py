#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    nums_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def solveSudoku(self, board):
        """ Hash and Backtracking.

        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # Pay Attention, can not define two-degree array as: [[0]*9]*9
        self.rows_hash, self.cols_hash = [[0] * 9 for i in range(9)], [[0] * 9 for i in range(9)]
        self.panel_hash = [[0] * 9 for i in range(9)]

        # Add all existing number to hash.
        for i in xrange(9):
            for j in xrange(9):
                if board[i][j] != ".":
                    self.try_num(int(board[i][j]) - 1, i, j)

        self.dfs_search(0, board)

    def dfs_search(self, cur, board):
        if cur == 81:
            return True
        r, c = cur / 9, cur % 9

        # The existing number must be valid, because we are promised that
        # there will be only one unique solution.
        if board[r][c] != ".":
            return self.dfs_search(cur + 1, board)

        else:
            for n in self.nums_list:
                if self.try_num(n - 1, r, c):
                    board[r][c] = str(n)
                    if self.dfs_search(cur + 1, board):
                        return True
                    # Remember to bacrtrack here.
                    board[r][c] = "."
                    self.backtrack(n - 1, r, c)
            return False

    def try_num(self, num, row, col):
        panel_pos = row / 3 * 3 + col / 3
        if (self.rows_hash[row][num] or self.cols_hash[col][num] or
                self.panel_hash[panel_pos][num]):
            return False
        else:
            self.rows_hash[row][num] = 1
            self.cols_hash[col][num] = 1
            self.panel_hash[panel_pos][num] = 1
            return True

    def backtrack(self, num, row, col):
        panel_pos = row / 3 * 3 + col / 3
        self.rows_hash[row][num] = 0
        self.cols_hash[col][num] = 0
        self.panel_hash[panel_pos][num] = 0

"""
["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
["53..7....","6..195...",".98....6.","8...6...3","4..8.3..1","7...2...6",".6....28.","...419..5","....8..79"]
"""
