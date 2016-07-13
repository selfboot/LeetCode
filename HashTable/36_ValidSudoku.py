#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def isValidSudoku(self, board):
        # check for rows
        for row in board:
            row_hash = {}
            for c in row:
                if c != "." and c in row_hash:
                    return False
                row_hash[c] = 1

        # check for cols
        for i in range(9):
            col_hash = {}
            for row in board:
                if row[i] != "." and row[i] in col_hash:
                    return False
                col_hash[row[i]] = 1

        # check for panel
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                count = 0
                panel_hash = {}
                while(count < 9):
                    c = board[i + count // 3][j + count % 3]
                    count += 1
                    if c != "." and c in panel_hash:
                        return False
                    panel_hash[c] = 1

        return True

"""
["..4...63.",".........","5......9.","...56....","4.3.....1","...7.....","...5.....",".........","........."]
[".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
"""
