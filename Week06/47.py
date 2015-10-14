#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def permuteUnique(self, nums):
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
            mark_num = []
            for num in nums:
                if num in mark_num:
                    continue
                else:
                    mark_num.append(num)

                no_num = nums[:]
                no_num.remove(num)
                no_num_permutations = self.permuteUnique(no_num)
                for each_permutation in no_num_permutations:
                    result = []
                    result.append(num)
                    result.extend(each_permutation)
                    permutations.append(result)

        return permutations
