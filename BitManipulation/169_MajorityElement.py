#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums) / 2]

    # Boyer–Moore majority vote algorithm. Refer to:
    # https://en.wikipedia.org/wiki/Boyer–Moore_majority_vote_algorithm
    def majorityElement_moore(self, nums):
        majority_num = 0
        count = 0
        for num in nums:
            if count == 0:
                majority_num = num
            if majority_num != num:
                count -= 1
            else:
                count += 1
        return majority_num

    # Hash table
    def majorityElement_hash(self, nums):
        num_len = len(nums)
        num_hash = {}
        for num in nums:
            num_hash[num] = num_hash.get(num, 0) + 1
            if num_hash[num] > num_len / 2:
                return num

    # Bit manipulation
    # Pay attention: in python -2147483648 >> 31 = -1
    def majorityElement_bit(self, nums):
        bit_bucket = [0 for i in range(33)]
        for num in nums:
            bit_bucket[32] += (num >> 32) & 1
            for i in range(32):
                bit_bucket[i] += (abs(num) >> i) & 1

        majority_num = 0
        nums_len = len(nums)
        for i in range(32):
            if bit_bucket[i] > nums_len / 2:
                majority_num += 1 << i
        if bit_bucket[32] > nums_len / 2:
            majority_num *= -1
        return majority_num

"""
[1]
[1]
[1,2,2,2]
[7,6,5,7,7]
[-2147483648]
[-2147483648, 2147483648, -2147483648]
[-1,-1,2147483647]
"""
