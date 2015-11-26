#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Refer to: https://leetcode.com/discuss/9476/solution-does-not-need-table-palindrome-right-uses-only-space
# A better solution


class Solution(object):
    """
    Dynamic Programming:
    """
    def minCut(self, s):
        s_len = len(s)
        # number of minnum cuts for the pre i characters
        min_cuts = [i-1 for i in range(s_len+1)]

        for i in range(s_len):
            # odd length palindrome
            j = 0
            while i-j >= 0 and i+j < s_len:
                if s[i-j] == s[i+j]:
                    min_cuts[i+j+1] = min(min_cuts[i+j+1], min_cuts[i-j]+1)
                    j += 1
                else:
                    break
            # even length palindrome
            j = 1
            while i-j+1 >= 0 and i+j < s_len:
                if s[i-j+1] == s[i+j]:
                    min_cuts[i+j+1] = min(min_cuts[i+j+1], min_cuts[i-j+1]+1)
                    j += 1
                else:
                    break

        return min_cuts[s_len]

"""
if __name__ == "__main__":
    sol = Solution()
    print sol.minCut("aab")
    print sol.minCut("aabb")
    print sol.minCut("aabaa")
    print sol.minCut("acbca")
    print sol.minCut("acbbca")
"""
