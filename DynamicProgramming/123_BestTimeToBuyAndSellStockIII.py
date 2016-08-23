#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        days_count = len(prices)
        pre_profit = [0] * days_count
        post_profit = [0] * days_count

        # Get max profit when buy and sell Stock only once in pre ith day.
        min_buy = prices[0]
        for i in range(1, days_count):
            min_buy = min(min_buy, prices[i])
            pre_profit[i] = max(pre_profit[i - 1], prices[i] - min_buy)

        # Get max profit when buy and sell Stock only once in post (n-i) days.
        max_sell = prices[-1]
        for j in range(days_count - 2, -1, -1):
            max_sell = max(max_sell, prices[j])
            post_profit[j] = max(post_profit[j + 1], max_sell - prices[j])

        # Find the max profit when buy and sell Stock only twice.
        # First in the pre kth day, and second in the post (n-k) days
        max_profit = 0
        for i in range(days_count):
            max_profit = max(max_profit, pre_profit[i] + post_profit[i])
        return max_profit


class Solution_2(object):
    """
    Assume we only have 0 money at first, Then
    sell_2: The maximum if we've just sold 2nd stock so far.
    buy_2: The maximum if we've just buy 2nd stock so far.
    sell_1: The maximum if we've just sold 1nd stock so far.
    buy_1: The maximum if we've just buy 1st stock so far.

    Refer to:
    https://discuss.leetcode.com/topic/5934/is-it-best-solution-with-o-n-o-1
    """
    def maxProfit(self, prices):
        buy_1, buy_2 = -2**31, -2**31
        sell_1, sell_2 = 0, 0
        for p in prices:
            sell_2 = max(sell_2, p + buy_2)
            buy_2 = max(buy_2, sell_1 - p)
            sell_1 = max(sell_1, p + buy_1)
            buy_1 = max(buy_1, -p)
        return sell_2

"""
[]
[1,2]
[1,3,5]
[2,8,3,9]
[2,8,3,9,1,2]
[2,8,3,9,1,9]
[6,5,4,3,2,1]
"""
