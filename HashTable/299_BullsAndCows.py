#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


class Solution(object):
    def getHint(self, secret, guess):
        secret = list(secret)
        guess = list(guess)

        bulls, cows = 0, 0
        hash_secret = {}
        hash_guess = {}
        for i in range(len(secret)):
            sec, gue = secret[i], guess[i]
            if sec == gue:
                bulls += 1
            else:
                hash_guess[gue] = hash_guess.get(gue, 0) + 1
                hash_secret[sec] = hash_secret.get(sec, 0) + 1
        for digit in hash_secret:
            if digit in hash_guess:
                cows += min(hash_guess[digit], hash_secret[digit])
        return "".join([str(bulls), "A", str(cows), "B"])


"""
""
""
"1807"
"7810"
"1123"
"1111"
"1123"
"0111"
"""
