#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# Obvious PUIQ(Point Update Interval Query) question.
# Can be solved with a fenwick tree（Binary Indexed Trees)
# Or use segment tree to solve it.


class NumArray(object):
    """
    1. Binary Indexed Trees.
    Here is the clear explanation about Binary Indexed Tree:
    http://blog.jobbole.com/96430/#
    """
    def __init__(self, nums):
        self.n = len(nums)
        self.nums = nums
        self.sum_tree = [0] * (self.n+1)
        for i in range(self.n):
            self._add(i+1, nums[i])

    def _add(self, i, val):
        while i <= self.n:
            self.sum_tree[i] += val
            i += (i & -i)

    # Get the sum of array nums[0:i], inclusive.
    def _sum(self, i):
        sum_val = 0
        while i > 0:
            sum_val += self.sum_tree[i]
            i -= (i & -i)
        return sum_val

    # Pay attention to the meanning of num & -num.
    # def _lowbit(self, num):
    #    return num & -num

    def update(self, i, val):
        self._add(i+1, val - self.nums[i])
        self.nums[i] = val

    def sumRange(self, i, j):
        if not self.nums:
            return 0
        # sum of elements nums[i..j], inclusive.
        return self._sum(j+1) - self._sum(i)

"""
if __name__ == '__main__':
    numArray = NumArray([1, 3, 5, 7, 8, 10])
    print numArray.sumRange(0, 4)
    numArray.update(1, 1)
    print numArray.sumRange(1, 3)
"""
