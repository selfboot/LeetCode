#! /usr/bin/env python
# -*- coding: utf-8 -*-
# According to: http://liangjiabin.com/blog/2015/04/leetcode-best-time-to-buy-and-sell-stock.html


class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        max_profit = 0
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i-1]
            if diff > 0:
                max_profit += diff
        return max_profit
"""
# Not readable.
class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        buy_price = prices[0]
        sell_price = buy_price
        max_profit = 0
        days = len(prices)
        ith_day = 1
        # Get the sum of every growth zone and
        # then we will get the best profit.
        while ith_day < days:
            if prices[ith_day] > sell_price:
                    sell_price = prices[ith_day]

            else:
                max_profit += sell_price - buy_price
                buy_price = prices[ith_day]
                sell_price = buy_price

            ith_day += 1
        max_profit += sell_price - buy_price
        return max_profit
"""

"""
[]
[3,4,5,6,2,4]
[6,5,4,3,2,1]
[1,2,3,4,3,2,1,9,11,2,20]
"""
