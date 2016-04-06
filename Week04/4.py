#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        length = len(nums1) + len(nums2)
        if length == 0:
            return 0

        if length & 0x1:
            return self.find_kth_num(nums1, nums2, (length + 1) / 2)
        else:
            return (self.find_kth_num(nums1, nums2, length / 2) +
                    self.find_kth_num(nums1, nums2, length / 2 + 1)) / 2.0

    # Find the kth number in sorted list: list1 , list2
    def find_kth_num(self, list_1, list_2, k):
        len_1 = len(list_1)
        len_2 = len(list_2)

        # Make sure k is largeer than the length of two lists
        if len_1 + len_2 < k:
            return None

        # Make sure the first list is always longer than the second
        if len_1 < len_2:
            return self.find_kth_num(list_2, list_1, k)
        if len_2 == 0:
            return list_1[k - 1]
        if k == 1:
            return min(list_1[0], list_2[0])

        # len_1 must be larger than half_k_1, because len_1 + len_2 >= k
        # but we shoud make sure half_k_2 < len_2
        # half_k_1 = min(k / 2, list_1)
        half_k_1 = max(k / 2, k - k / 2)
        half_k_2 = min(k - half_k_1, len_2)
        if list_1[half_k_1 - 1] < list_2[half_k_2 - 1]:
            return self.find_kth_num(list_1[half_k_1:],
                                     list_2, k - half_k_1)
        elif list_1[half_k_1 - 1] > list_2[half_k_2 - 1]:
            return self.find_kth_num(list_1, list_2[half_k_2:],
                                     k - half_k_2)
        else:
            return list_1[half_k_1 - 1]

"""
[]
[1]
[1]
[2,3,4,5,6]
[2,3,4]
[5,6,7]
"""
