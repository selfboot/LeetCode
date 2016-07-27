#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# @Last Modified time: 2016-07-27 09:43:06


class Solution(object):
    def addOperators(self, num, target):
        """ Once you can understand the solution space tree, you just get it.

        Refer to:
        https://discuss.leetcode.com/topic/24523/java-standard-backtrace-ac-solutoin-short-and-clear
        """
        ans = []
        self.dfs_search(ans, "", num, target, 0, 0, 0)
        return ans

    def dfs_search(self, ans, path, num, target, pos, pre_num, value):
        """  Put binary operator in pos, and then calculate the new value.

        @pre_num: when process *, we need to know the previous number.
        """
        if pos == len(num):
            if value == target:
                ans.append(path)
            return

        for i in range(pos + 1, len(num) + 1):
            cur_str, cur_n = num[pos: i], int(num[pos: i])
            # Digit can not begin with 0 (01, 00, 02 are not valid), except 0 itself.
            if i > pos + 1 and num[pos] == '0':
                break
            if pos == 0:
                self.dfs_search(ans, path + cur_str, num, target, i, cur_n, cur_n)
            # All three different binary operators: +, -, *
            else:
                self.dfs_search(ans, path + "+" + cur_str, num,
                                target, i, cur_n, value + cur_n)
                self.dfs_search(ans, path + "-" + cur_str, num,
                                target, i, -cur_n, value - cur_n)
                self.dfs_search(ans, path + "*" + cur_str, num,
                                target, i, pre_num * cur_n, value - pre_num + pre_num * cur_n)

"""
"000"
0
"123"
6
"232"
8
"1005"
5
"3456237490"
9191
"""
