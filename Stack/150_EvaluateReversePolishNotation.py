#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def evalRPN(self, tokens):
        value_stack = []
        for token in tokens:
            if token in "+-*/":
                operand_2 = value_stack.pop()
                operand_1 = value_stack.pop()
                negative = 1
                if operand_1 * operand_2 < 0:
                    negative = -1

                if token == "+":
                    result = operand_1 + operand_2
                elif token == "-":
                    result = operand_1 - operand_2
                elif token == "*":
                    result = operand_1 * operand_2
                else:
                    # Leetcode think 12/-7 = -1, 12/-13 = 0
                    result = abs(operand_1) / abs(operand_2) * negative

                value_stack.append(result)
            else:
                value_stack.append(int(token))
        return value_stack[-1]

"""
["18"]
["12", "-7", "/"]
["2", "1", "+", "3", "*"]
["4", "13", "5", "/", "+"]
"""
