#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


class Solution(object):
    def maxProduct(self, words):
        max_product = 0
        length = len(words)
        bit_record = [0] * length
        # Use 1bit to represent each letter, and
        # use 32bit(Int variable, bitMap[i]) to represent the set of each word
        for i in xrange(length):
            for c in words[i]:
                bit_record[i] |= 1 << (ord(c) - ord("a"))

        for i in xrange(length):
            for j in xrange(i+1, length):
                # If the AND of two bitmap element equals to 0,
                # these two words do not have same letter.
                if not bit_record[i] & bit_record[j]:
                    product = len(words[i]) * len(words[j])
                    if product > max_product:
                        max_product = product
        return max_product

"""
[]
["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
["a", "aa", "aaa", "aaaa"]
"""
