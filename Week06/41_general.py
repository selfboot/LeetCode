#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1

        min_num = max_num = 0
        missing_mid = []
        first_positive = 0
        for num in nums:
            first_positive += 1
            if num > 0:
                min_num = max_num = num
                break

        for num in nums[first_positive:]:
            if num <= 0:
                pass
            elif num > max_num:
                for integer in range(max_num + 1, num):
                    missing_mid.append(integer)
                max_num = num
            elif num < min_num:
                for integer in range(num + 1, min_num):
                    missing_mid.append(integer)
                min_num = num
            else:
                if num in missing_mid:
                    missing_mid.remove(num)

        missing_mid.sort()
        if min_num > 1:
            return 1
        if missing_mid:
            return missing_mid[0]
        else:
            return max_num + 1
