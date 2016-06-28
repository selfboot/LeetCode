#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def getPermutation(self, n, k):
        """According to:

        https://leetcode.com/discuss/42700/explain-like-im-five-java-solution-in-o-n
        The logic is as follows:
        For n-th numbers, the permutations can be divided into (n-1)! groups,
        For the n-1 th numbers, can be divided to (n-2)! groups, and so on.
        Thus k/(n-1)! indicates the index of current number,
        and k%(n-1)! denotes remaining index for the remaining n-1 numbers.
        We keep doing this until n reaches 0, then we get n numbers permutations that is kth.
        """
        factorial = [1] * n
        for i in xrange(1, n):
            factorial[i] = i * factorial[i - 1]

        if k > factorial[n - 1] * n or k <= 0:
            return -1

        remain_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        result, pos, k = [], n, k - 1
        while pos:
            cur_num = k / factorial[pos - 1]
            k %= factorial[pos - 1]
            target_num = remain_list[cur_num]
            remain_list.remove(target_num)
            result.append(str(target_num))
            pos -= 1

        return "".join(result)

"""
9
23
9
24
9
25
"""
