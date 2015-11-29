#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    """
    Dynamic Programming
    dp[i]: if s[i:] can be broken to wordDict. then:
    dp[i-1] = s[i:i+k] in wordDict and dp[i+k+1], for all the possible k.
    """
    def wordBreak(self, s, wordDict):
        if not s:
            return [""]

        self.s_len = len(s)
        self.result = []
        self.str = s
        self.words = wordDict

        dp = [False for i in range(self.s_len + 1)]
        dp[-1] = True

        for i in range(self.s_len - 1, -1, -1):
            k = 0
            while k + i < self.s_len:
                cur_fisrt_word = self.str[i:i+k+1]
                if cur_fisrt_word in self.words and dp[i + k + 1]:
                    dp[i] = True
                    break

                k += 1

        self.word_break(0, [], dp)
        return self.result

    # Depth First Search
    def word_break(self, start, word_list, dp):
        if start == self.s_len:
            self.result.append(" ".join(word_list))
            return

        k = 0
        while start+k < self.s_len:
            cur_word = self.str[start:start+k+1]
            if cur_word in self.words and dp[start+k+1]:
                word_list.append(cur_word)
                self.word_break(start+k+1, word_list, dp)
                word_list.pop()
            k += 1
"""
"a"
[]
""
[]
"catsanddog"
["cat","cats","and","sand","dog"]
"leetcode"
["leet", "code", "lee", "t"]
"""
