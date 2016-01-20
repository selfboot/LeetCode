#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


class Solution(object):
    def containsDuplicate(self, nums):
        hash_dict = {}
        for num in nums:
            if num in hash_dict:
                return True
            hash_dict[num] = 1
        return False

"""
[]
[1,2,3,3]
[1,2,3,4,1]
"""
