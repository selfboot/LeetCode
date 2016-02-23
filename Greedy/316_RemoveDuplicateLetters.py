#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# Refer to:
# https://leetcode.com/discuss/73777/easy-to-understand-iterative-java-solution


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        Given the string s, the greedy choice is the smallest s[i],
        s.t. the suffix s[i .. ] contains all the unique letters.
        After determining the greedy choice s[i], get a new string by:
            1. removing all letters to the left of s[i],
            2. removing all s[i] in s[i+1:].
        We then recursively solve the sub problem s'.
        """

        if not s:
            return ""

        # 1. Find out the last appeared position for each letter;
        char_dict = {}
        for i, c in enumerate(s):
            char_dict[c] = i

        # 2. Find out the smallest index (2) from the map in step 1;
        pos = len(s)
        for i in char_dict.values():
            if i < pos:
                pos = i

        # 3. The first letter in the final result must be
        #    the smallest letter from index 0 to index (2);
        char = s[0]
        res_pos = 0
        for i in range(1, pos+1):
            if s[i] < char:
                char = s[i]
                res_pos = i
        # 4. Find out remaining letters with the new s.
        new_s = [c for c in s[res_pos+1:] if c != char]
        return char + self.removeDuplicateLetters("".join(new_s))


# Use Stack to avoid recursive, more quickly.
class Solution_2(object):
    def removeDuplicateLetters(self, s):
        char_dict = {}
        used = {}
        for c in s:
            char_dict[c] = char_dict.get(c, 0) + 1
            used[c] = False

        res = []        # Use as a Stack.
        for c in s:
            char_dict[c] -= 1
            if used[c]:
                continue

            while res and res[-1] > c and char_dict[res[-1]] > 0:
                used[res[-1]] = False
                res.pop()

            res.append(c)
            used[c] = True
        return "".join(res)

"""
""
"bcabc"
"abacb"
"cbacdcbc"
"""
