#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    # Method easy to understand
    def isIsomorphic(self, s, t):
        if not s:
            return True
        str_len = len(s)

        # s --> t
        replace_hash = {}
        for i in range(str_len):
            if s[i] not in replace_hash:
                replace_hash[s[i]] = t[i]
            else:
                if replace_hash[s[i]] == t[i]:
                    pass
                else:
                    return False
        # t --> s
        replace_hash_2 = {}
        for i in range(str_len):
            if t[i] not in replace_hash_2:
                replace_hash_2[t[i]] = s[i]
            else:
                if replace_hash_2[t[i]] == s[i]:
                    pass
                else:
                    return False

        return True

    # According to
    # https://leetcode.com/discuss/48674/python-different-solutions-dictionary-etc
    # Pythonic way, smarter, fastest.
    def isIsomorphic_2(self, s, t):
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))

    # More generic way
    def isIsomorphic_3(self, s, t):
        s_l, t_l = [-1] * 256, [-1] * 256
        str_len = len(s)
        for i in range(str_len):
            if s_l[ord(s[i])] != t_l[ord(t[i])]:
                return False
            s_l[ord(s[i])], t_l[ord(t[i])] = i, i
        return True

    # Another pythonic way, slower
    def isIsomorphic_4(self, s, t):
        return [s.find(i) for i in s] == [t.find(j) for j in t]
        # return map(s.find, s) == map(t.find, t)

"""
""
""
"ab"
"aa"
"foo"
"bar"
"egg"
"add"
"""
