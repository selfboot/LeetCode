#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    """ Same as "max subarray problem" using Kadane's Algorithm.

    Just need one scan through the array values,
    computing at each position the max profit ending at that position.
    https://en.wikipedia.org/wiki/Maximum_subarray_problem
    """
    def maxProfit(self, prices):
        if not prices:
            return 0
        max_profit = 0
        min_buy = prices[0]
        for price in prices:
            min_buy = min(price, min_buy)
            max_profit = max(price - min_buy, max_profit)
        return max_profit


class Solution_2(object):
    """
    sell_1: The maximum if we've just sold 1nd stock so far.
    buy_1: The maximum if we've just buy 1st stock so far.

    Then we can update sell_1 if p + buy_1(sell now) get more than pre-sell_1.
    And update buy_1 if remain more money when we buy now than pre-buy_1.
    Here update sell_1 before buy_1 because we need to use pre_buy_1 to get sell_1.
    """
    def maxProfit(self, prices):
        sell_1, buy_1 = 0, -2**31
        for p in prices:
            sell_1 = max(sell_1, p + buy_1)
            buy_1 = max(buy_1, -p)
        return sell_1

"""
[]
[3,4,5,6,2,4]
[6,5,4,3,2,1]
[1,2,3,4,3,2,1,9,11,2,20]
"""
