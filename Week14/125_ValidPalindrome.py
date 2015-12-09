#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        alpha_num_str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        s = s.upper()
        s_l = len(s)
        pre = 0
        post = s_l - 1
        while pre < post and pre < s_l and post >= 0:
            # Remember the situation ",,..".
            # Make sure pre and post don't
            while pre < s_l and s[pre] not in alpha_num_str:
                pre += 1
            while post >= 0 and s[post] not in alpha_num_str:
                post -= 1
            if pre >= post:
                break
            if s[pre] != s[post]:
                return False
            pre += 1
            post -= 1

        return True

"""
""
"1a2"
",,,,...."
"A man, a plan, a canal: Panama"
"race a car"
"""
