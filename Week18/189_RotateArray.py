#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    # 1. Make an extra copy and then rotate.
    def rotate(self, nums, k):
        if not nums or k <= 0:
            return
        nums_copy = nums[:]
        n = len(nums)
        for i in range(n):
            nums[(i+k) % n] = nums_copy[i]

    # 2. Simple three reverse.
    # Reverse all the n elements, the first k elements,
    # and then the last n-k elements.
    def rotate_1(self, nums, k):
        if not nums or k <= 0:
            return
        n = len(nums)
        k = k % n
        nums.reverse()
        self.reverse_part(nums, 0, k-1)
        self.reverse_part(nums, k, n-1)

    def reverse_part(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    """
    3. Swap the last k elements with the first k elements.
       The last k elements will be in the correct positions.
       but we need to rotate the remaining (n - k) elements
       to the right position.
       Now we need to rotate(nums[k:], k), then keep rotating
    """
    def rotate_2(self, nums, k):
        if not nums or k <= 0:
            return
        n = len(nums)
        k = k % n
        start = 0
        while k:
            for i in range(k):
                nums[start+i], nums[start+n-k+i] = (
                    nums[start+n-k+i], nums[start+i])
            start += k
            n = n - k
            k = k % n

"""
[1]
0
[1,2]
1
[1,2,3,4,5,6,7]
3
[1,2,3,4,5,6,7]
10
"""
