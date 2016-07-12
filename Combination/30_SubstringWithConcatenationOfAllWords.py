#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# @Last Modified time: 2016-07-12 18:57:50


class Solution(object):
    """ Easy to think, but is very slow.

    Use an unordered_map<string, int> counts to record the expected times of each word and
    another unordered_map<string, int> seen to record the times we have seen
    """

    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_cnt = {}
        for w in words:
            word_cnt[w] = word_cnt.get(w, 0) + 1

        s_len, word_l = len(s), len(words[0])
        concatenation_l = len(words) * word_l
        ans = []
        for i in range(s_len - concatenation_l + 1):
            candidate_map = {}
            j = 0
            while j < len(words):
                w = s[i + j * word_l: i + (j + 1) * word_l]
                if w not in word_cnt:
                    break
                candidate_map[w] = candidate_map.get(w, 0) + 1
                if candidate_map.get(w, 0) > word_cnt[w]:
                    break
                j += 1

            if j == len(words):
                ans.append(i)

        return ans


class Solution_2(object):
    """ Use hashmap and two point.

    Travel all the words combinations to maintain a slicing window.
    There are wl(word len) times travel, each time n/wl words:
    mostly 2 times travel for each word:
        one left side of the window, the other right side of the window
    So, time complexity O(wl * 2 * N/wl) = O(2N)
    Refer to:
    https://discuss.leetcode.com/topic/6617/an-o-n-solution-with-detailed-explanation
    """
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_cnt = {}
        for w in words:
            word_cnt[w] = word_cnt.get(w, 0) + 1

        s_len, w_len, cnt = len(s), len(words[0]), len(words)
        i = 0
        ans = []
        while i < w_len:
            left, count = i, 0
            candidate_cnt = {}
            for j in range(i, s_len, w_len):
                cur_str = s[j: j + w_len]
                if cur_str in word_cnt:
                    candidate_cnt[cur_str] = candidate_cnt.get(cur_str, 0) + 1
                    count += 1
                    if candidate_cnt[cur_str] <= word_cnt[cur_str]:
                        pass
                    else:
                        # A more word, advance the window left side possiablly
                        while candidate_cnt[cur_str] > word_cnt[cur_str]:
                            left_str = s[left: left + w_len]
                            candidate_cnt[left_str] -= 1
                            left += w_len
                            count -= 1

                    # come to a result
                    if count == cnt:
                        ans.append(left)
                        candidate_cnt[s[left:left + w_len]] -= 1
                        count -= 1
                        left += w_len
                # not a valid word, clear the window.
                else:
                    candidate_cnt = {}
                    left = j + w_len
                    count = 0
            i += 1
        return ans


class Solution_Fail(object):
    """ Pythonic way, easy to think, but Time Limit Exceeded.

    Use two hash-map.
    """
    def findSubstring(self, s, words):
        if not s or not words:
            return []
        import collections
        word_cnt = collections.Counter(words)
        s_len, word_l = len(s), len(words[0])
        concatenation_l = len(words) * word_l
        ans = []
        for i in range(s_len - concatenation_l + 1):
            candidate_str = s[i:i + concatenation_l]
            split_str = [candidate_str[j:j + word_l]
                         for j in range(0, concatenation_l, word_l)]
            candidate_cnt = collections.Counter(split_str)
            if not (word_cnt - candidate_cnt):
                ans.append(i)
        return ans

"""
""
[]
"barfoothefoobarman"
["foo", "bar"]
"barfoofoobarthefoobarman"
["bar","foo","the"]
"""
