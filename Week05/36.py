#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        columns = ["" for i in range(9)]
        panes = ["" for i in range(9)]

        for i in range(9):

            # Check row
            row = board[i]
            if self.isRepeat(row):
                return False

            # Get columns
            for j in range(9):
                columns[j] += row[j]

            # Get pane
            for k in range(9):
                pane_row = i / 3
                pane_col = k / 3
                pos = pane_row * 3 + pane_col
                panes[pos] += row[k]

        # Check columns
        for col in columns:
            if self.isRepeat(col):
                return False

        # Check panes
        for pane in panes:
            if self.isRepeat(pane):
                return False

        return True

    def isRepeat(self, board_str):
        flag = [0 for i in range(9)]
        for i in range(9):
            if board_str[i] == ".":
                continue
            num = ord(board_str[i]) - ord("0") - 1
            if flag[num]:
                return True
            else:
                flag[num] = 1

        return False
