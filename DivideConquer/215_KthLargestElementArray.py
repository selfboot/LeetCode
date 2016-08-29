#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


class Solution(object):
    # Simple way: O(nlogn)
    def findKthLargest(self, nums, k):
        return sorted(nums)[-k]


class Solution_2(object):
    # QuickSelect, according to:
    # http://www.cs.yale.edu/homes/aspnes/pinewiki/QuickSelect.html
    # Heap implement by c++ can be found in c++ version.
    def findKthLargest(self, nums, k):
        pivot = nums[0]
        nums1, nums2 = [], []
        for num in nums:
            if num > pivot:
                nums1.append(num)
            elif num < pivot:
                nums2.append(num)
        if k <= len(nums1):
            return self.findKthLargest(nums1, k)
        elif k > len(nums) - len(nums2):
            return self.findKthLargest(nums2, k - (len(nums) - len(nums2)))
        else:
            return pivot

"""
[1]
1
[3,2,1,5,6,4]
2
[1,2,1,3,9]
2
"""
