#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# @Last Modified time: 2016-07-04 12:05:02


class Solution(object):
    def reverseVowels(self, s):
        # Scan while incrementing start and decrementing end.
        all_vowels = set(['a', 'e', 'i', 'o', 'u',
                          'A', 'E', 'I', 'O', 'U'])
        s = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] in all_vowels and s[right] in all_vowels:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            elif s[left] in all_vowels:
                right -= 1
            elif s[right] in all_vowels:
                left += 1
            else:
                left += 1
                right -= 1
        return "".join(s)

"""
""
"hello"
"leetcode"
"Administrator"
"""
