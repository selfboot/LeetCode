#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        len_s = len(s)
        max_valid_start_i = [0 for i in range(len_s + 1)]

        start_i = len_s - 2
        while(start_i >= 0):

            if s[start_i] == ")":
                max_valid_start_i[i] = 0
                start_i -= 1
                continue

            if s[start_i + 1] == ")":
                if start_i + 2 < len_s:
                    max_valid_start_i[start_i] = 2 + max_valid_start_i[start_i + 2]
                else:
                    max_valid_start_i[start_i] = 2
            else:
                next_start = start_i + 2 + max_valid_start_i[start_i + 1]

                if next_start - 1 <= len_s - 1 and s[next_start - 1] == ")":
                    max_valid_start_i[start_i] = 2 + max_valid_start_i[start_i + 1]
                    if next_start <= len_s - 1:
                        max_valid_start_i[start_i] += max_valid_start_i[next_start]
                else:
                    max_valid_start_i[start_i] = 0

            start_i -= 1

        max_len = 0
        for length in max_valid_start_i:
            if length > max_len:
                max_len = length

        return max_len

# if __name__ == "__main__":
#     sol = Solution()
#     print sol.longestValidParentheses("(((()()()))(")
#     print sol.longestValidParentheses("(((()()()))())")
#     print sol.longestValidParentheses("())()()()")
#     print sol.longestValidParentheses("(((()()()))(((")
#     print sol.longestValidParentheses("(((((()()())))")
