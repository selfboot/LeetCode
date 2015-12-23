#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def countPrimes(self, n):
        if n <= 2:
            return 0
        count = 1
        # nums = [1 for i in range(n)]
        # Faster as follows
        nums = [1] * n

        for num in range(3, n, 2):
            if nums[num] == 1:
                count += 1
                k = num
                while num * k < n:
                    nums[num*k] = 0
                    k += 1
            else:
                pass
        return count

    # Pythonic way, beats 98% submissions.
    def countPrimes_2(self, n):
        if n <= 2:
            return 0
        nums = [True] * n
        nums[:2] = [False] * 2
        nums[2:n:2] = [False] * ((n-1)/2)
        for i in range(3, int(n ** 0.5) + 1, 2):
            if nums[i]:
                nums[i*i:n:i] = [False] * ((n-i*i-1)/i+1)

        return sum(nums)+1

"""
0
120
9999
"""
