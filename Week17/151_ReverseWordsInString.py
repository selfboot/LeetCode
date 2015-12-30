#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def reverseWords(self, s):
        return " ".join(s.split()[::-1])

"""
if __name__ == "__main__":
    sol = Solution()
    print sol.reverseWords("AAA BBB   ")
    print sol.reverseWords(" BBB   CC  ")
"""
