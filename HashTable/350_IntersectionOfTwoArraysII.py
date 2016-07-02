#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# @Last Modified time: 2016-07-02 10:47:23


class Solution(object):
    def intersect(self, nums1, nums2):
        nums1_dict = {}
        for n in nums1:
            nums1_dict[n] = nums1_dict.get(n, 0) + 1
        ans = []
        for n in nums2:
            if nums1_dict.get(n, 0) > 0:
                ans.append(n)
                nums1_dict[n] = nums1_dict.get(n, 0) - 1
        return ans


class Solution_2(object):
    def intersect(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        ans = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                ans.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return ans

"""
[]
[]
[1,2,2,2,3]
[3,2,2,2,3]
[1, 2, 2, 1]
[2, 2]
"""
