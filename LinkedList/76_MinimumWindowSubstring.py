#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def minWindow(self, s, t):
        s_size = len(s)
        if not t or not s:
            return ""

        # Keep the present tims of all characters in T.
        t_dict = {}
        for char in t:
            if char not in t_dict:
                t_dict[char] = 1
            else:
                t_dict[char] += 1

        count = 0
        t_size = len(t)
        start = end = 0
        # min_window(start, end): the suitable window's left and right board
        min_window = (0, s_size)
        # Keep the present tims of the window's characters that appear in T.
        win_dict = {}
        while end < s_size:
            cur_char = s[end]
            if cur_char in t_dict:
                if cur_char not in win_dict:
                    win_dict[cur_char] = 1
                else:
                    win_dict[cur_char] += 1
                if win_dict[cur_char] <= t_dict[cur_char]:
                    count += 1

            if count == t_size:
                # Move start toward to cut the window's size.
                is_suitable_window = True
                while start <= end and is_suitable_window:
                    start_char = s[start]
                    if start_char not in t_dict:
                        start += 1
                    else:
                        if win_dict[start_char] > t_dict[start_char]:
                            win_dict[start_char] -= 1
                            start += 1
                        else:
                            is_suitable_window = False

                # Update the minimum window
                window_size = end - start + 1
                min_size = min_window[1] - min_window[0] + 1
                if window_size < min_size:
                    min_window = (start, end)

                # Move start toward to find another suitable window
                win_dict[s[start]] -= 1
                start += 1
                count -= 1

            end += 1
        # No suitable window
        if min_window[1] == s_size:
            return ""
        return s[min_window[0]: min_window[1] + 1]

"""
"a"
""
"ADOBECODEBANC"
"ABCC"
"""
