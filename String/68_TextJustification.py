#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def fullJustify(self, words, maxWidth):
        """ Straightforward solution for the problem

        Refer to:
        https://discuss.leetcode.com/topic/25970/concise-python-solution-10-lines

        Once you determine that there are only k words that can fit on a given line,
        you know what the total length of those words is cur_letters.
        Then the rest are spaces, and there are L = (maxWidth - cur_letters) of spaces.

        The trick here is to use mod operation to manage the spaces.
        The "or 1" part is for dealing with the edge case len(cur) == 1.
        """
        ans, cur_words, cur_letters = [], [], 0
        for w in words:
            if len(cur_words) + cur_letters + len(w) > maxWidth:
                pad_space_cnt = maxWidth - cur_letters
                for i in range(pad_space_cnt):
                    cur_words[i % (len(cur_words) - 1 or 1)] += ' '
                ans.append(''.join(cur_words))

                cur_words, cur_letters = [], 0

            cur_words.append(w)
            cur_letters += len(w)

        return ans + [' '.join(cur_words).ljust(maxWidth)]

"""
["a"]
1
[""]
2
["This", "is", "an", "example", "of", "text", "justification."]
15
["This", "is", "an", "example", "of", "text", "justification."]
16
["This", "is", "an", "example", "of", "text", "justification."]
20
["What","must","be","shall","be."]
12
"""
