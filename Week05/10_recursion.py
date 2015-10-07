#! /usr/bin/env python
# -*- coding: utf-8 -*-


"""
According the article in LeetCode:
http://articles.leetcode.com/2011/09/regular-expression-matching.html
"""


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        print s, p
        if not p:
            return s == ""
        # Optimized for the specified case:
        # "aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"
        if len(s) > 0 and s[-1] != p[-1] and p[-1] != "*" and p[-1] != ".":
            return False

        """
        If the next character of p is NOT ‘*’,
        then it must match the current character of s.
        Continue pattern matching with the next character of both s and p.
        """
        if len(p) == 1 or p[1] != "*":
            # assert p[0] != "*"
            if s == "" or (p[0] != "." and s[0] != p[0]):
                return False

            return self.isMatch(s[1:], p[1:])

        """
        If the next character of p is ‘*’,
        then we do a brute force exhaustive matching of 0, 1,
        or more repeats of current character of p…
        Until we could not match any more characters.
        """
        if len(p) > 1 and p[1] == "*":
            # assert p[0] != "*"
            next_p = p[2:]

            if s == "":
                return self.isMatch(s, next_p)

            # a* match 0 of the preceding character in s
            if p[0] != s[0] and p[0] != ".":
                return self.isMatch(s, next_p)

            # a brute force exhaustive matching of 0, 1, 2, ...
            index = 0
            while index < len(s) and (s[index] == p[0] or p[0] == "."):
                next_s = s[index:]
                if self.isMatch(next_s, next_p):
                    return True
                index += 1
            return self.isMatch(s[index:], next_p)

# if __name__ == '__main__':
#    so = Solution()
#    print so.isMatch("aaa", "ab*a")    # False
#    print so.isMatch("", "c*c*")       # True
#    print so.isMatch("aaa", "aaaa")    # False
#    print so.isMatch("aaabc", "a*bc")  # True
#    print so.isMatch("aab", "c*a*b")   # True
#    print so.isMatch("ab", ".*c")      # False
#    print so.isMatch("aaaaabaccbbccababa", "a*b*.*c*c*.*.*.*c")  # False
#    print so.isMatch("aabbcbcacbacaaccacc", "c*b*b*.*.*.*a*.*")  # True
#    print so.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c")  # False
