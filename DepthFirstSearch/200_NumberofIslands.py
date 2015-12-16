#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0
        island_counts = 0
        self.m_rows = len(grid)
        self.n_cols = len(grid[0])
        self.grid = grid

        island_counts = 0
        for i in range(self.m_rows):
            for j in range(self.n_cols):
                if grid[i][j] == "1":
                    island_counts += 1
                    self.merge_surround(i, j)

        return island_counts

    # Depth First Search
    # Merge all the adjacent islands to one island.
    def merge_surround(self, i, j):
        if self.grid[i][j] == "1" or self.grid[i][j] == "#":
            if i+1 < self.m_rows and self.grid[i+1][j] == "1":
                self.grid[i+1][j] = "#"
                self.merge_surround(i+1, j)
            if j+1 < self.n_cols and self.grid[i][j+1] == "1":
                self.grid[i][j+1] = "#"
                self.merge_surround(i, j+1)
            if i-1 >= 0 and self.grid[i-1][j] == "1":
                self.grid[i-1][j] = "#"
                self.merge_surround(i-1, j)
            if j-1 >= 0 and self.grid[i][j-1] == "1":
                self.grid[i][j-1] = "#"
                self.merge_surround(i, j-1)
        return

"""
["1"]
["111","010","111"]
["111", "100", "101", "111"]
["11110", "11010", "11000", "00000"]
["11000", "11000", "00100", "00011"]
"""
