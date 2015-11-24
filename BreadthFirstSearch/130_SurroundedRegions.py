#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m_rows = len(board)
        n_cols = len(board[0])
        if m_rows <= 2 or n_cols <= 2:
            return

        for row in range(m_rows):
            board[row] = list(board[row])

        # Search from the first and last row
        for i in [0, m_rows-1]:
            for j in range(n_cols):
                if board[i][j] == "O":
                    self.breadth_first_search(i, j, board)

        # Search from the first and last column
        for j in [0, n_cols-1]:
            for i in range(m_rows):
                if board[i][j] == "O":
                    self.breadth_first_search(i, j, board)

        # Make all the O surrounded by X to be X
        for i in range(m_rows):
            for j in range(n_cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "#":
                    board[i][j] = "O"
            board[i] = "".join(board[i])

    """
    Mark all the Os can be arrived from outside row(column) to be '#'
    And return one O node's adjacent O nodes
    """
    def set_adjacency(self, row, col, board):
        board[row][col] = "#"
        adjacency_node = []
        m_rows = len(board)
        n_cols = len(board[0])
        if row - 1 >= 0 and board[row-1][col] == "O":
            board[row-1][col] = "#"
            adjacency_node.append([row-1, col])
        if row + 1 < m_rows and board[row+1][col] == "O":
            board[row+1][col] = "#"
            adjacency_node.append([row+1, col])
        if col - 1 >= 0 and board[row][col-1] == "O":
            board[row][col-1] = "#"
            adjacency_node.append([row, col-1])
        if col + 1 < n_cols and board[row][col+1] == "O":
            board[row][col+1] = "#"
            adjacency_node.append([row, col+1])
        return adjacency_node

    # Do BFS to every out border O ndoe.
    def breadth_first_search(self, row, col, board):
        adjacency_nodes = self.set_adjacency(row, col, board)
        adjacency_record = []
        while adjacency_nodes:
            for node in adjacency_nodes:
                adjacency_record.extend(
                    self.set_adjacency(node[0], node[1], board))
            adjacency_nodes = adjacency_record
            adjacency_record = []
"""
[]
["XXX", "XOX", "XXX"]
["OOX", "XOX", "OXX"]
["XXXX", "XOOX", "XXOX", "XOXX"]
"""
