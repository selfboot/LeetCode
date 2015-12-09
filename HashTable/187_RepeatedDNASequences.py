#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        str_hash = {}
        sequence = []
        len_s = len(s)
        for i in range(len_s-9):
            cur_str = s[i:i+10]
            str_hash[cur_str] = str_hash.get(cur_str, 0) + 1
            if str_hash[cur_str] == 2:
                sequence.append(cur_str)
        return sequence


"""
"AAA"
"AAAAAAAAAA"
"AAAAAAAAAAA"
"AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
"""
