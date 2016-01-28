#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


class Solution(object):
    def gameOfLife(self, board):
        if not board:
            return
        m_rows = len(board)
        n_cols = len(board[0])
        count = [[0 for j in range(n_cols)] for i in range(m_rows)]
        for i in range(m_rows):
            for j in range(n_cols):
                # Compute the number of live neighbors and
                # Update the count of adjancent next cells meanwhile.
                if j+1 < n_cols:
                    count[i][j] += board[i][j+1]
                    count[i][j+1] += board[i][j]
                if i+1 < m_rows:
                    count[i][j] += board[i+1][j]
                    count[i+1][j] += board[i][j]
                    if j-1 >= 0:
                        count[i][j] += board[i+1][j-1]
                        count[i+1][j-1] += board[i][j]
                    if j+1 < n_cols:
                        count[i][j] += board[i+1][j+1]
                        count[i+1][j+1] += board[i][j]
                # Current cell interacts with its eight neighbors
                # Live cell turn dead
                if board[i][j] and (count[i][j] < 2 or count[i][j] > 3):
                    board[i][j] = 0
                # Dead cell turn live
                if not board[i][j] and count[i][j] == 3:
                    board[i][j] = 1
        return

"""
[[]]
[[0]]
[[1,1],[0,1]]
[[0,1,0],[1,1,1],[0,1,0]]
"""
