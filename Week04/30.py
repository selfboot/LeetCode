#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words:
            return []

        words_dict = {}
        for word in words:
            if word in words_dict:
                words_dict[word] += 1
            else:
                words_dict[word] = 1

        sol_list = []
        s_len = len(s)
        w_len = len(words[0])
        words_len = len(words) * w_len
        start_index = 0
        while start_index <= s_len - words_len:

            w_count = 0
            w_dict = {}
            while w_count < words_len:
                start = start_index + w_count
                cur_w = s[start: start + w_len]
                if cur_w not in words:
                    w_dict = {}
                    break

                if cur_w in w_dict:
                    w_dict[cur_w] += 1
                else:
                    w_dict[cur_w] = 1

                if w_dict[cur_w] > words_dict[cur_w]:
                    w_dict = {}
                    break
                w_count += w_len

            if w_count == words_len:
                sol_list.append(start_index)
            start_index += 1

        return sol_list
