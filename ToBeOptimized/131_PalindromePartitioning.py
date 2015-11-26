#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def partition(self, s):
        if not s:
            return []
        self.result = []
        self.end = len(s)
        self.str = s

        self.is_palindrome = [[False for i in range(self.end)]
                              for j in range(self.end)]

        for i in range(self.end-1, -1, -1):
            for j in range(self.end):
                if i > j:
                    pass
                elif j-i < 2 and s[i] == s[j]:
                    self.is_palindrome[i][j] = True
                elif self.is_palindrome[i+1][j-1] and s[i] == s[j]:
                    self.is_palindrome[i][j] = True
                else:
                    self.is_palindrome[i][j] = False

        self.palindrome_partition(0, [])
        return self.result

    def palindrome_partition(self, start, sub_strs):
        if start == self.end:
            # It's confused the following sentence doesn't work.
            # self.result.append(sub_strs)
            self.result.append(sub_strs[:])
            return

        for i in range(start, self.end):
            if self.is_palindrome[start][i]:
                sub_strs.append(self.str[start:i+1])
                self.palindrome_partition(i+1, sub_strs)
                sub_strs.pop()      # Backtracking here


if __name__ == "__main__":
    sol = Solution()
    print sol.partition("aab")
    print sol.partition("aabb")
    print sol.partition("aabaa")
    print sol.partition("acbca")
    print sol.partition("acbbca")

