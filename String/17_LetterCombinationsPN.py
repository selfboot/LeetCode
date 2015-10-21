#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        phone_letters = {0: [" "],
                         1: ["*"],
                         2: ["a", "b", "c"],
                         3: ["d", "e", "f"],
                         4: ["g", "h", "i"],
                         5: ["j", "k", "l"],
                         6: ["m", "n", "o"],
                         7: ["p", "q", "r", "s"],
                         8: ["t", "u", "v"],
                         9: ["w", "x", "y", "z"],
                         }
        if digits:
            all_str = phone_letters[ord(digits[0]) - ord("0")]
        else:
            return []

        for i in range(1, len(digits)):
            all_str = self.combination(
                all_str,
                phone_letters[ord(digits[i]) - ord("0")])

        return all_str

    # return string which combines a in str_a with b in str_b
    def combination(self, str_a, str_b):
        combine_str = []
        for a in str_a:
            for b in str_b:
                combine_str.append(a + b)

        return combine_str

"""
""
"37"
"1234"
"""
