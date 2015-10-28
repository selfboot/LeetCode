#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if words == [""]:
            return [" " * maxWidth]

        len_current_words = 0
        count_current_words = 0
        lines_justifi = []
        current_line = []
        for word in words:
            len_w = len(word)
            if len_current_words + len_w + count_current_words <= maxWidth:
                len_current_words += len_w
                count_current_words += 1
                current_line.append(word)
            else:
                # Finish the old line and get the justification string.
                one_line = self.convert_line(len_current_words,
                                             current_line,
                                             count_current_words,
                                             maxWidth,
                                             False)
                lines_justifi.append(one_line)

                # Start a new line
                current_line = []
                current_line.append(word)
                len_current_words = len_w
                count_current_words = 1

        # For the last line;
        one_line = self.convert_line(len_current_words,
                                     current_line,
                                     count_current_words,
                                     maxWidth,
                                     True)
        lines_justifi.append(one_line)

        return lines_justifi

    # Finish the text Justification job
    def convert_line(self, len_current_words,
                     current_line, count_current_words, maxWidth, last_line):
        one_line = ""
        # Process the last line in partucularly
        if last_line:
            for i in range(count_current_words-1):
                one_line += current_line[i]
                one_line += " "
            one_line += current_line[count_current_words-1]
            line_len = len(one_line)
            one_line += " " * (maxWidth - line_len)
            return one_line

        assert(count_current_words != 0)
        if count_current_words > 1:
            spaces_need = maxWidth - len_current_words
            averge_space = spaces_need / (count_current_words - 1)
            spaces_more = spaces_need % (count_current_words - 1)
            for i in range(spaces_more):
                one_line += current_line[i]
                one_line += " " * (averge_space + 1)
            for i in range(spaces_more, count_current_words-1):
                one_line += current_line[i]
                one_line += " " * averge_space
            one_line += current_line[count_current_words-1]
        else:
            char_len = len(current_line[0])
            one_line = current_line[0] + " " * (maxWidth - char_len)

        return one_line
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
