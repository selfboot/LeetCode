#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def exist(self, board, word):
        if not board and word:
            return False
        if not word:
            return True

        m_rows = len(board)
        n_cols = len(board[0])
        for row in range(m_rows):
            for col in range(n_cols):
                if board[row][col] == word[0]:
                    board[row][col] = "*"
                    if (self.exist_adjacent(
                            [row, col],
                            word[1:],
                            board)):
                        return True
                    # Backtracking here
                    board[row][col] = word[0]
        return False

    def exist_adjacent(self, cur_pos, next_str, board):
        # Find all the characters in word.
        if not next_str:
            return True

        adj_pos = self.adj_pos_lists(cur_pos, board)
        # No adjancent position can be used.
        if not adj_pos:
            return False

        # For every adjacent position, find out whether it contains
        # the first character in the word or not.
        # If matches, then resursively check the other characters in word.
        for pos in adj_pos:
            row = pos[0]
            col = pos[1]
            if board[row][col] == next_str[0]:
                board[row][col] = "*"
                if (self.exist_adjacent(
                        [row, col],
                        next_str[1:],
                        board)):
                    return True
                # Backtracking here
                board[row][col] = next_str[0]

        return False

    # Find the adjacent position around cur_pos
    def adj_pos_lists(self, cur_pos, board):
        m_rows = len(board)
        n_cols = len(board[0])
        row = cur_pos[0]
        col = cur_pos[1]
        adj_list = []
        if row - 1 >= 0:
            adj_list.append([row - 1, col])
        if row + 1 < m_rows:
            adj_list.append([row + 1, col])
        if col - 1 >= 0:
            adj_list.append([row, col - 1])
        if col + 1 < n_cols:
            adj_list.append([row, col + 1])
        return adj_list

"""
[]
""
[]
"as"
["abce","sfcs", "adee"]
"abcced"
["abce","sfcs", "adee"]
"abcb"
["ABCE","SFES","ADEE"]
"ABCESEEEFSAD"
"""
