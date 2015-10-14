#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1_long = int(num1)
        num2_long = int(num2)
        return str(num1_long * num2_long)
