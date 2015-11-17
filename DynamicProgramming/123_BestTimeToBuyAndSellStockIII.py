#! /usr/bin/env python
# -*- coding: utf-8 -*-
# According to: http://liangjiabin.com/blog/2015/04/leetcode-best-time-to-buy-and-sell-stock.html


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        days_count = len(prices)
        pre_profit = [0 for i in range(days_count)]
        post_profit = [0 for j in range(days_count)]

        # Get max profit when buy and sell Stock only once in pre ith day.
        min_buy = prices[0]
        for i in range(1, days_count):
            min_buy = min(min_buy, prices[i])
            pre_profit[i] = max(pre_profit[i-1], prices[i]-min_buy)

        # Get max profit when buy and sell Stock only once in post (n-i) days.
        max_sell = prices[-1]
        for j in range(days_count-2, -1, -1):
            max_sell = max(max_sell, prices[j])
            post_profit[j] = max(post_profit[j+1], max_sell-prices[j])

        # Find the max profit when buy and sell Stock only twice.
        # First in the pre kth day, and second in the post (n-k) days
        max_profit = 0
        for i in range(days_count):
            max_profit = max(max_profit, pre_profit[i] + post_profit[i])
        return max_profit

"""
[]
[1,2]
[1,3,5]
[2,8,3,9]
[2,8,3,9,1,2]
[2,8,3,9,1,9]
[6,5,4,3,2,1]
"""
