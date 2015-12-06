#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    """
    Radix sort, you can see the explanation follow the links.
    https://www.cs.usfca.edu/~galles/visualization/RadixSort.html
    And here is a java solution in leetcode's discuss:
    https://leetcode.com/discuss/53636/radix-sort-solution-in-java-with-explanation
    """
    def maximumGap(self, nums):
        if not nums:
            return 0

        max_gap = 0
        max_num = nums[0]
        for num in nums:
            if num > max_num:
                max_num = num

        exp = 1
        sorted_digit = [0 for num in nums]
        while max_num / exp > 0:
            digits = [0 for i in range(10)]
            for num in nums:
                digits[(num/exp) % 10] += 1
            for i in range(1, 10):
                digits[i] += digits[i-1]
            for num in nums[::-1]:
                digit_num = (num/exp) % 10
                sorted_digit[digits[digit_num]-1] = num
                digits[digit_num] -= 1
            nums = sorted_digit
            exp *= 10

        max_gap = 0
        for i in range(1, len(nums)):
            max_gap = max(max_gap, nums[i]-nums[i-1])
        return max_gap

"""
[]
[1]
[9,12,4,8,6,16,23]
[2,99999999]
"""
