#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1_left = 0
        nums2_left = 0

        # Set 0 to the redundant space
        for i in range(m + n, len(nums1)):
            nums1[i] = 0

        while nums1_left < m + n and nums2_left < n:
            # All the number in nums1 is in the suitable position
            if not m or nums1_left == m + nums2_left:
                nums1[nums1_left] = nums2[nums2_left]
                nums1_left += 1
                nums2_left += 1

            # nums1 don't need to change, just move toward
            elif nums2[nums2_left] > nums1[nums1_left]:
                nums1_left += 1

            # add the number in nums2 into nums1
            else:
                val_2 = nums2[nums2_left]
                val_1 = nums1[nums1_left]
                nums1[nums1_left] = val_2
                nums1_left += 1
                for i in range(m + nums2_left, nums1_left, -1):
                    nums1[i] = nums1[i - 1]
                nums1[nums1_left] = val_1
                nums2_left += 1
"""
[1,2,3,0,0,0]
3
[2,5,6]
3
[3,5,7,8,9,10,0,0,0,0]
5
[2,4,6,7]
4
"""
