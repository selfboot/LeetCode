#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def maxProduct(self, nums):
        if not nums:
            return 0

        max_num = small = big = nums[0]
        for num in nums[1:]:
            small, big = (
                min(num, small*num, big*num),
                max(num, small*num, big*num)
                )
            max_num = max(max_num, big)

        return max_num

        """ Somewhat complex and hard to understand.
        n_len = len(nums)
        if n_len == 1:
            return nums[0]

        dp = [[0, 0] for i in nums]
        if nums[0] >= 0:
            dp[0] = [nums[0], None]
        else:
            dp[0] = [None, nums[0]]

        max_product = nums[0]
        for i in range(1, n_len):
            if nums[i] < 0:
                dp[i][1] = nums[i]
                if dp[i-1][1]:
                    dp[i][0] = max(dp[i-1][1] * nums[i], dp[i][1])
                if dp[i-1][0]:
                    dp[i][1] = min(dp[i-1][0] * nums[i], nums[i])
            elif nums[i] > 0:
                dp[i][0] = nums[i]
                if dp[i-1][0]:
                    dp[i][0] = max(dp[i-1][0] * nums[i], dp[i][0])
                if dp[i-1][1]:
                    dp[i][1] = min(dp[i-1][1] * nums[i], nums[i])
            else:
                dp[i] = [0, None]

            max_product = max(dp[i][0], max_product)

        return max_product
        """

"""
[]
[-2]
[-2,-3]
[-2,0,-1]
[6,3,-10,0,2]
[1,0,-2,-3,5]
"""
