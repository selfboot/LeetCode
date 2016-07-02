#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# @Last Modified time: 2016-07-01 21:00:38


class Solution(object):
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))


class Solution_2(object):
    def intersection(self, nums1, nums2):
        ans = []
        nums1_dict = {}
        for n in nums1:
            nums1_dict[n] = nums1_dict.get(n, 0) + 1

        for n in nums2:
            if n in nums1_dict and nums1_dict[n] != -1:
                ans.append(n)
                nums1_dict[n] = -1
        return ans


class Solution_3(object):
    def intersection(self, nums1, nums2):
        # sort the two list, and use two pointer to search to find common elements.
        ans = []
        nums1.sort()
        nums2.sort()
        i = j = 0
        while (i < len(nums1) and j < len(nums2)):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                if not len(ans) or nums1[i] != ans[-1]:
                    ans.append(nums1[i])
                i += 1
                j += 1

        return ans

"""
[]
[]
[-1]
[]
[1,2,2,2,10,5]
[1,3,4,5,9]
"""
