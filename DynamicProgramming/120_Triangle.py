#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0

        triangle_l = len(triangle)
        dp = [0 for i in range(triangle_l)]
        dp[0] = triangle[0][0]
        min_path_sum = dp[0]
        for row in range(1, triangle_l):
            # keep the changed path
            keep_num = dp[0]
            nums_row = triangle[row]
            row_l = len(nums_row)

            if row == triangle_l - 1:
                min_path_sum = dp[0] + triangle[row][0]

            for j in range(row_l):
                left_path = "a"
                up_path = "a"
                if j-1 >= 0:
                    left_path = keep_num + triangle[row][j]
                if j < row_l - 1:
                    up_path = dp[j] + triangle[row][j]

                keep_num = dp[j]
                # Get the min path of the current row's position
                if left_path != "a" and up_path != "a":
                    min_path = min(left_path, up_path)
                elif left_path == "a":
                    min_path = up_path
                else:
                    min_path = left_path
                dp[j] = min_path
                # Find the minest path sum
                if row == triangle_l - 1:
                    min_path_sum = min(dp[j], min_path_sum)
        return min_path_sum

"""
[]
[[-10]]
[[2],[3,4],[6,5,7],[1,4,8,3]]
[[2],[3,3],[1,5,0],[4,6,9,3]]
"""
