#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def longestValidParentheses(self, s):
        """
        According to:
        https://leetcode.com/discuss/7609/my-o-n-solution-using-a-stack

        If current character is '(', push its index to the stack.
        If current character is ')':
        1. top of stack is '(', just find a matching pair so pop from the stack.
        2. Otherwise, we push the index of ')' to the stack.

        Finally the stack will only contain the indices of characters which cannot be matched.
        Then the substring between adjacent indices should be valid parentheses.
        """
        stack, longest = [0], 0
        for i in xrange(1, len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                    valid_len = (i - stack[-1]) if stack else i + 1
                    longest = max(longest, valid_len)
                else:
                    stack.append(i)
        return longest

"""
""
")"
"()"
"))"
"(((()()()))("
"(((()()()))())"
"""
