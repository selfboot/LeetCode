#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


class Solution(object):
    def isAnagram(self, s, t):
        char_hash = {}
        for c in s:
            char_hash[c] = char_hash.get(c, 0) + 1

        for c in t:
            if c not in char_hash:
                return False
            char_hash[c] -= 1
            if char_hash[c] < 0:
                return False
        return not sum(char_hash.values())

"""
""
""
"acd"
"ac"
"anagram"
"nagaram"
"rat"
"car"
"""
