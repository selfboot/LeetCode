#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    # Refer to:
    # https://leetcode.com/discuss/25603/a-concise-dp-solution-in-java
    def maxProfit(self, k, prices):
        if not prices:
            return 0
        days_num = len(prices)
        if k == 0 or days_num < 2:
            return 0
        # There is no limit on transaction's times in fact.
        if k/2 > days_num:
            return self.max_profits(prices)

        # dp[i][j] is the max profit for up to i transactions by days j.
        # 0 < i <= K, 0 <= j < das_num.
        # tmp_max: max profit for up to i transactions, last buy on day j-1.
        dp = [[0 for day in range(days_num)] for trans in range(k+1)]
        for trans in range(1, k+1):
            tmp_max = -prices[0]
            for day in range(1, days_num):
                dp[trans][day] = max(dp[trans][day-1], prices[day] + tmp_max)
                tmp_max = max(tmp_max, dp[trans-1][day-1] - prices[day])
        return dp[k][days_num-1]

    # Get the max profits without the limit of transactions.
    def max_profits(self, prices):
        profits = 0
        days_num = len(prices)
        for i in range(1, days_num):
            price_diff = prices[i] - prices[i-1]
            if price_diff > 0:
                profits += price_diff
        return profits

"""
1
[8,5,3]
2
[1,8,3,2,7,12,7,15,16,17]
4
[1,8,3,2,7,12,7,15,16,17]
"""
