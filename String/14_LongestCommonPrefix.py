#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        common_prefix = strs[0]
        for string in strs:
            min_len = min(len(string), len(common_prefix))
            mark = 0        # Record the longest commen prefix index right now.
            for i in range(min_len):
                mark = i
                if string[i] == common_prefix[i]:
                    i += 1
                    mark = i
                else:
                    if i == 0:
                        return ""
                    break
            common_prefix = common_prefix[:mark]

        return common_prefix

"""
[]
["abcd", "abc", "ab","acdef"]
["abc", "abcd", "d"]
"""
