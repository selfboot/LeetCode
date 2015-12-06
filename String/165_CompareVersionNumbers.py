#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def compareVersion(self, version1, version2):
        ver_list_1 = version1.split(".")
        ver_list_2 = version2.split(".")

        len_1 = len(ver_list_1)
        len_2 = len(ver_list_2)
        for i in range(len_1):
            ver_list_1[i] = int(ver_list_1[i])
        for i in range(len_2):
            ver_list_2[i] = int(ver_list_2[i])

        len_max = max(len_1, len_2)
        for i in range(len_1, len_max):
            ver_list_1.append(0)
        for i in range(len_2, len_max):
            ver_list_2.append(0)

        for i in range(len_max):
            if ver_list_1[i] < ver_list_2[i]:
                return -1
            elif ver_list_1[i] > ver_list_2[i]:
                return 1
            else:
                pass
        return 0

"""
"01"
"1"
"1.0"
"1"
"1.2.3.4"
"1.2.3.4.5"
"1.12.13"
"1.13"
"""
