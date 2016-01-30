#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


class Solution(object):
    """
    Violent search: Generate all possible states by removing one ( or ),
    check if they are valid.  It is something like Breadth First Search.
    Easy to understand but slower.
    """
    def removeInvalidParentheses(self, s):
        unvalid_str = {s}
        # unvalid_str = set(s)  Wrong initinal way.

        # Every time we go into the iteration,
        # We delete one more parentheses then check all the possible situation.
        while True:
            valid = filter(self.isvalid, unvalid_str)
            if valid:
                return valid
            else:
                new_set = set()
                for str in unvalid_str:
                    for i in range(len(str)):
                        new_set.add(str[:i] + str[i+1:])
                unvalid_str = new_set

    def isvalid(self, str):
        count = 0
        for c in str:
            if c == "(":
                count += 1
            elif c == ")":
                count -= 1
                if count < 0:
                    return False
            else:
                pass

        return count == 0


class Solution_2(object):
    """
    Depth First Search with backtrack.
    Generate new strings by removing parenthesis,
    and calculate the total number of mismatched parentheses.
        1. If the mismatched parentheses increased, then go back.
        2. Otherwise, remove parentheses until have no mismatched parentheses.
    """
    def removeInvalidParentheses(self, s):
        self.visited = {s}   # self.visited = set([s])
        return self.dfsRemove(s)

    def dfsRemove(self, s):
        count = self.mismatchedCount(s)
        if count == 0:
            return [s]

        result = []
        for i in range(len(s)):
            if s[i] not in "()":
                continue
            # Remove one ( or )
            new = s[:i] + s[i+1:]
            if new not in self.visited and self.mismatchedCount(new) < count:
                self.visited.add(new)
                result.extend(self.dfsRemove(new))
        return result

    def mismatchedCount(self, s):
        """
        Get the total number of mismatched parentheses in string s.
        Actually it's the minimum number of parentheses we need to remove.
        """
        mis_l, mis_r = 0, 0
        for ch in s:
            if ch == "(":
                mis_l += 1
            elif ch == ")":
                mis_l -= 1
                mis_r += (mis_l < 0)
                mis_l = max(mis_l, 0)
            else:
                pass
        return mis_l + mis_r


class Solution_3(object):
    """
    The fastest one.  According to:
    https://leetcode.com/discuss/82300/44ms-python-solution
    The main point is:
        1. Scan from left to right, make sure count["("]>=count[")"].
        2. Then scan from right to left, make sure count["("]<=count[")"].
    """
    def removeInvalidParentheses(self, s):
        possibles = {s}
        count = {"(": 0, ")": 0}
        removed = 0

        # Scan s from left to right to remove mismatched ).
        for i, ch in enumerate(s):
            # Remove pre or current ) to make count["("] >= count[")"]
            if ch == ")" and count["("] == count[")"]:
                new_possible = set()
                while possibles:
                    j = 0
                    str = possibles.pop()
                    while j + removed <= i:
                        if str[j] == ")":
                            new_possible.add(str[:j] + str[j+1:])
                        j += 1
                possibles = new_possible
                removed += 1
            elif ch in count:
                count[ch] += 1
            else:
                pass

        # Scan possibles from right to left to remove mismatched (.
        count = {"(": 0, ")": 0}
        possible_len = len(s) - removed
        pos = len(s)
        for i in range(possible_len-1, -1, -1):
            # !!! Attention: all mismatched ( appear after mismatched ).
            pos -= 1
            ch = s[pos]
            # Remove post or current ( to make count["("] <= count[")"]
            if ch == "(" and count["("] == count[")"]:
                new_possible = set()
                while possibles:
                    str = possibles.pop()
                    j = i
                    while j < len(str):
                        if str[j] == "(":
                            new_possible.add(str[:j] + str[j+1:])
                        j += 1
                possibles = new_possible
            elif ch in count:
                count[ch] += 1
            else:
                pass

        return list(possibles)

"""
""
")("
")))"
"((("
")()("
"())))"
"()())()"
"(a)())()"
"""
