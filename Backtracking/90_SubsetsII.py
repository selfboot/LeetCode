#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if not nums:
            return []

        nums.sort()
        nums_len = len(nums)

        # Keep the subsets without duplicate subsets
        subsets = [[nums[0]]]
        # Keep the previous subsets which contains previous nums.
        pre_subset = [[nums[0]]]

        for i in range(1, nums_len):
            # Combine current num with the previous subsets,
            # Then update the previous subsets
            if nums[i] == nums[i-1]:
                for j in range(len(pre_subset)):
                    one_set = pre_subset[j][:]
                    one_set.append(nums[i])
                    subsets.append(one_set)
                    pre_subset[j] = one_set

            # Combine current num with all the subsets before.
            # Then update the previous subsets
            else:
                pre_subset = []
                for j in range(len(subsets)):
                    one_set = subsets[j][:]
                    one_set.append(nums[i])
                    subsets.append(one_set)
                    pre_subset.append(one_set)
                pre_subset.append([nums[i]])
                subsets.append([nums[i]])

        subsets.append([])
        return subsets

"""
[]
[1,2]
[1,2,2]
[1,2,2,3,3,4,5]
"""
