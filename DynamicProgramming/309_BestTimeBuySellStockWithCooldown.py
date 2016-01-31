#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com


class Solution(object):
    """
    Dynamic Programming.
    A very good explanation come with thinking process is here:
    https://leetcode.com/discuss/71354/share-my-thinking-process

    States definition:
        buy[i]: The maxProfit for any sequence end with buy in pre i days.
        sell[i]: The maxProfit for any sequence end with sell in pre i days.
    Transition function (price is the price of day i):
        buy[i] = max(buy[i-1], sell[i-2] - price)
        sell[i] = max(sell[i-1], buy[i-1] + price)
    To get buy[i](sell[i] is the same), there are two possibilities:
        1. No transaction on day i, then buy[i] = buy[i-1]
        2. Buy stock on day i, last sell must berofe i-1 day,
           then buy[i] = sell[i-2] - price
    """
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        # There is no need to use array to keep the states. O(1) space is OK.
        pre_buy, buy, pre_sell, sell = -prices[0], 0, 0, 0
        for cur_price in prices[1:]:
            # Here pre_sell is euqal sell[i-2], sell is equal sell[i-1]
            buy = max(pre_sell - cur_price, pre_buy)
            pre_sell = sell
            sell = max(pre_buy + cur_price, pre_sell)
            pre_buy = buy
        return sell

"""
[]
[1,2,3,0,2]
[1,2,5,0,2]
[1,2,5,0,8]
"""
