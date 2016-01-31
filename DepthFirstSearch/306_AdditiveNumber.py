#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


class Solution(object):
    # According to:
    # https://leetcode.com/discuss/70089/python-solution
    # The key point is choose first two number then recursively check.
    # DFS: recursice implement.
    def isAdditiveNumber(self, num):
        length = len(num)
        for i in range(1, length/2+1):
            for j in range(1, (length-i)/2 + 1):
                first, second, others = num[:i], num[i:i+j], num[i+j:]
                if self.isValid(first, second, others):
                    return True
        return False

    def isValid(self, first, second, others):
        # Numbers in the additive sequence cannot have leading zeros,
        if ((len(first) > 1 and first[0] == "0") or
                (len(second) > 1 and second[0] == "0")):
            return False
        sum_str = str(int(first) + int(second))
        if sum_str == others:
            return True
        elif others.startswith(sum_str):
            return self.isValid(second, sum_str, others[len(sum_str):])
        else:
            return False


class Solution_2(object):
    # DFS: iterative implement.
    def isAdditiveNumber(self, num):
        length = len(num)
        for i in range(1, length/2+1):
            for j in range(1, (length-i)/2 + 1):
                first, second, others = num[:i], num[i:i+j], num[i+j:]
                if ((len(first) > 1 and first[0] == "0") or
                        (len(second) > 1 and second[0] == "0")):
                    continue

                while others:
                    sum_str = str(int(first) + int(second))
                    if sum_str == others:
                        return True
                    elif others.startswith(sum_str):
                        first, second, others = (
                            second, sum_str, others[len(sum_str):])
                    else:
                        break

        return False

"""
"1123"
"1203"
"112324"
"112334"
"112358"
"""
