#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# @Last Modified time: 2016-06-26 19:18:40


class Solution(object):
    def groupAnagrams(self, strs):
        """Hash tables: use sorted(word) as key.

        Note that list is unhashable type, so we need to change sorted
        str to tuple, which is hashable type.
        """
        d = {}
        for w in sorted(strs):
            key = tuple(sorted(w))
            d[key] = d.get(key, []) + [w]
        return d.values()

"""
[""]
["aaa", "aaa", "aa", "bb"]
["a", "b", "c", "d"]
"""
