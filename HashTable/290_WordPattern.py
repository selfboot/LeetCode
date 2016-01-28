#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


class Solution(object):
    def wordPattern(self, pattern, str):
        words = str.split(" ")
        if len(pattern) != len(words):
            return False

        char_word = {}
        for i, char in enumerate(pattern):
            if char in char_word and char_word[char] != words[i]:
                return False
            if char not in char_word:
                char_word[char] = words[i]

        word_char = {}
        for j, word in enumerate(words):
            if word in word_char and word_char[word] != pattern[j]:
                return False
            if word not in word_char:
                word_char[word] = pattern[j]
        return True

"""
""
""
"a"
"are"
"abba"
"dog cat cat dog"
"abb"
"dog cat cat"
"aba"
"dog dog dog"
"""
