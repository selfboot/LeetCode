#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]

        permutations = []
        if len(nums) == 1:
            result = []
            result.append(nums[0])
            permutations.append(result)

        else:
            for num in nums:
                no_num = nums[:]
                no_num.remove(num)
                no_num_permutations = self.permute(no_num)
                for each_permutation in no_num_permutations:
                    result = []
                    result.append(num)
                    result.extend(each_permutation)
                    permutations.append(result)

        return permutations
