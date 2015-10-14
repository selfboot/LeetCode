#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"
        num1, num2 = num1[::-1], num2[::-1]
        length = len(num1) + len(num2)
        mul_integer = [0 for i in range(length - 1)]

        # Get the sum of each two digit, and keep the sum in int[i + j],
        # We can make sure mul[i + j] max to be 81 * len(num),
        # which can be stored in int: 2 ^ 31 - 1
        for i in range(len(num1)):
            for j in range(len(num2)):
                integer_i = int(num1[i])
                integer_j = int(num2[j])
                mul_integer[i + j] += integer_i * integer_j

        # Put the sum into str
        mul_str = ""
        carry = 0
        for integer in mul_integer:
            digit = (integer + carry) % 10
            mul_str = str(digit) + mul_str
            carry = (integer + carry) / 10

        mul_str = str(carry) + mul_str

        # Count the numbers of pre zero
        zero_count = 0
        for char in mul_str:
            if char != "0":
                break
            zero_count += 1

        return mul_str[zero_count:]

