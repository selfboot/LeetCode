#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    """
    Dynamic Programming:
    cuts[i]: minimum cuts needed for a palindrome partitioning of s[i:]
    is_palindrome[i][j]: whether s[i:i+1] is palindrome
    """
    def minCut(self, s):
        if not s:
            return 0
        s_len = len(s)

        is_palindrome = [[False for i in range(s_len)]
                         for j in range(s_len)]

        cuts = [s_len-1-i for i in range(s_len)]
        for i in range(s_len-1, -1, -1):
            for j in range(i, s_len):
                # if self.is_palindrome(i, j):
                if ((j-i < 2 and s[i] == s[j]) or
                        (s[i] == s[j] and is_palindrome[i+1][j-1])):
                    is_palindrome[i][j] = True
                    if j == s_len - 1:
                        cuts[i] = 0
                    else:
                        cuts[i] = min(cuts[i], 1+cuts[j+1])
                else:
                    pass

        return cuts[0]

"""
if __name__ == "__main__":
    sol = Solution()
    print sol.minCut("aab")
    print sol.minCut("aabb")
    print sol.minCut("aabaa")
    print sol.minCut("acbca")
    print sol.minCut("acbbca")
"""
