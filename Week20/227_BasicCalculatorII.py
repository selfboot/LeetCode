#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# According to:
# https://leetcode.com/discuss/53554/python-short-solution-with-stack


class Solution(object):
    # Stack
    def calculate(self, s):
        num_stack = []
        num = 0
        sign = "+"
        for i in xrange(len(s)):
            ch = s[i]
            if ch.isdigit():
                num = num * 10 + ord(ch) - ord('0')
            if not ch.isdigit() and ch != " " or i == len(s) - 1:
                if sign == "+":
                    num_stack.append(num)
                elif sign == "-":
                    num_stack.append(-num)
                elif sign == "*":
                    num_stack.append(num * num_stack.pop())
                else:
                    tmp = num_stack.pop()
                    divid = tmp / num
                    if tmp / num < 0 and tmp % num != 0:
                        divid += 1
                    num_stack.append(divid)
                sign = ch
                num = 0
        return sum(num_stack)

"""
# No Stack
# Refer to a very smart solution
# https://leetcode.com/discuss/41641/17-lines-c-easy-20-ms
class Solution(object):
    def calculate(self, s):
        s = "".join(s.split(" "))
        s = "+" + s + "+"
        len_s = len(s)
        result, term = 0, 0
        i = 0
        while i < len_s:
            ch = s[i]
            if ch in "+-":
                result += term
                term = 0
                i += 1
                while i < len_s and s[i] not in "+-*/":
                    term = term * 10 + int(s[i])
                    i += 1
                term *= 1 if ch == "+" else -1
            else:
                new_term = 0
                i += 1
                while i < len_s and s[i] not in "+-*/":
                    new_term = new_term * 10 + int(s[i])
                    i += 1
                # For python: -3/2 = -2, which isn't suitable here.
                # We need -3/2 = -1, because 14-3/2 = 13 not 12.
                oper = 1
                if term < 0:
                    oper *= -1
                    term *= -1
                if ch == "/":
                    term /= new_term
                else:
                    term *= new_term
                term *= oper
        return result
"""

"""
if __name__ == '__main__':
    sol = Solution()
    print sol.calculate("3112 ")
    print sol.calculate("3+ 2 * 2/1 *2")
    print sol.calculate(" 14- 3/  2")
    print sol.calculate("3 + 50 / 2")
"""
