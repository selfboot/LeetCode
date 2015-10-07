#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        stack = []
        for i in range(len(s)):
            char = s[i]
            if char == "(":
                stack.append([char, i])

            else:
                if stack and stack[-1][0] == "(":
                    del stack[-1]
                    if stack:
                        max_len = max(max_len, i - stack[-1][1])
                    else:
                        max_len = max(max_len, i + 1)
                else:
                    stack.append([char, i])
            i += 1

        return max_len

# if __name__ == "__main__":
#     sol = Solution()
#     print sol.longestValidParentheses("(((()()()))(")
#     print sol.longestValidParentheses("(((()()()))())")
#     print sol.longestValidParentheses("())()()()")
#     print sol.longestValidParentheses("()()()")
#     print sol.longestValidParentheses("(((()()()))(((")
#     print sol.longestValidParentheses("(((((()()())))")
"""
10
14
6
6
10
12
"""
