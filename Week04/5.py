#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        processed_s = ""
        if not s:
            return ""

        for char in s:
            processed_s = processed_s + char + "#"
        processed_s = "^" + processed_s[:-1] + "$"
        length = len(processed_s)
        count = [0 for x in range(length)]

        longest_index = 1
        left_index = longest_index - count[longest_index]
        for index in range(2, length - 2):
            if index - longest_index >= count[longest_index]:
                pan_count = 0
                while (processed_s[index - pan_count - 1] != "^"
                       and processed_s[index + pan_count + 1] != "$"
                       and processed_s[index - pan_count - 1]
                       == processed_s[index + pan_count + 1]):
                    pan_count += 1

                count[index] = pan_count
                if pan_count > count[longest_index]:
                    longest_index = index
                    left_index = longest_index - pan_count
                if pan_count == count[longest_index]:
                    if (pan_count % 2 == 1 and processed_s[index] == "#") or\
                       (pan_count % 2 == 0 and processed_s[index] != "#"):
                        longest_index = index
                        left_index = longest_index - pan_count

            else:
                sym_index = 2 * longest_index - index
                if sym_index - left_index > count[sym_index]:
                    count[index] = count[sym_index]
                else:
                    pan_count = sym_index - left_index
                    while (processed_s[index - pan_count - 1] != "^"
                           and processed_s[index + pan_count + 1] != "$"
                           and processed_s[index - pan_count - 1]
                           == processed_s[index + pan_count + 1]):
                        pan_count += 1

                    count[index] = pan_count
                    if pan_count > count[longest_index]:
                        longest_index = index
                        left_index = longest_index - pan_count
                    if pan_count == count[longest_index]:
                        if (pan_count % 2 == 1 and processed_s[index] == "#") or\
                           (pan_count % 2 == 0 and processed_s[index] != "#"):
                            longest_index = index
                            left_index = longest_index - pan_count

            # print index, longest_index, count[index]
            index += 1

        if processed_s[longest_index] == "#":
            mid_index = longest_index / 2 - 1
            max_len = (count[longest_index] - 1) / 2
            return s[mid_index - max_len: mid_index + max_len + 2]

        else:
            mid_index = (longest_index + 1) / 2 - 1
            max_len = count[longest_index] / 2
            return s[mid_index - max_len: mid_index + max_len + 1]

if __name__ == "__main__":
    sol = Solution()
#    print sol.longestPalindrome("ccd")
#    print sol.longestPalindrome("cccd")
    print sol.longestPalindrome("dcc")
#    print sol.longestPalindrome("dccc")
#    print sol.longestPalindrome("edcde")
#    print sol.longestPalindrome("a")
#    print sol.longestPalindrome("aa")
#    print sol.longestPalindrome("aaaa")
#    print sol.longestPalindrome("fedcdeg")
#    print sol.longestPalindrome("edccde")
#    print sol.longestPalindrome("fedccdeg")
