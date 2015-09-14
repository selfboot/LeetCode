#! /usr/bin/env python
# -*- coding: utf-8 -*-


def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """

    length = len(s)
    palindrome_record = [[0 for col in range(length)] for row in range(length)]

    start = 0
    end = 0
    # length of the palindrome is less than 2
    for i in range(length):
        palindrome_record[i][i] = 1

        if i + 1 < length and s[i] == s[i + 1]:
            palindrome_record[i][i + 1] = 1
            start = i
            end = i + 1

    # length of the palindrome is growing to len(s)
    for len_of_palidrome in range(3, length + 1):
        for i in range(length - len_of_palidrome + 1):
            j = i + len_of_palidrome - 1
            if palindrome_record[i + 1][j - 1] and s[i] == s[j]:
                palindrome_record[i][j] = 1
                start = i
                end = i + len_of_palidrome

    return s[start: end + 1]


if __name__ == "__main__":
    print longestPalindrome("abacdcaba")
