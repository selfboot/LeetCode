#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        close_s = ""
        for symbol in s:
            if symbol == "(":
                close_s = ")" + close_s

            elif symbol == "[":
                close_s = "]" + close_s

            elif symbol == "{":
                close_s = "}" + close_s

            elif symbol == ")":
                if close_s and close_s[0] == ")":
                    close_s = close_s[1:]
                    continue
                else:
                    return False
            elif symbol == "]":
                if close_s and close_s[0] == "]":
                    close_s = close_s[1:]
                    continue
                else:
                    return False
            else:
                if close_s and close_s[0] == "}":
                    close_s = close_s[1:]
                    continue
                else:
                    return False
        if close_s == "":
            return True
        else:
            return False
