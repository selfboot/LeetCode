#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


class Solution(object):
    # According to Wiki: Digital root
    # https://en.wikipedia.org/wiki/Digital_root
    def addDigits(self, num):
        if not num:
            return 0
        return (1+(num-1) % 9)
