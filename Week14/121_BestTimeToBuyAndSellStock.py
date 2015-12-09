#! /usr/bin/env python
# -*- coding: utf-8 -*-
# According to: http://liangjiabin.com/blog/2015/04/leetcode-best-time-to-buy-and-sell-stock.html


class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        max_profit = 0
        min_buy = prices[0]
        for price in prices:
            min_buy = min(price, min_buy)
            max_profit = max(price-min_buy, max_profit)
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
        while ith_day < days:
            # The current price is higher than the cost we buy,
            # so just keep the stock, until the price is lower.
            if prices[ith_day] >= buy_price:
                # make the price that we sell the stock be biggest
                if prices[ith_day] > sell_price:
                    sell_price = prices[ith_day]
                else:
                    pass
            # Meet a new lower price, so buy the stock
            else:
                max_profit = max(max_profit, sell_price - buy_price)
                buy_price = prices[ith_day]
                sell_price = buy_price

            ith_day += 1
        # The price may never be lower than the first day.
        max_profit = max(max_profit, sell_price - buy_price)
        return max_profit
"""

"""
[]
[3,4,5,6,2,4]
[6,5,4,3,2,1]
[1,2,3,4,3,2,1,9,11,2,20]
"""
