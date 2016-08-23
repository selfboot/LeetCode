# @Author: xuezaigds@gmail.com
# @Last Modified time: 2016-08-23 14:17:12
# -*- coding: utf-8 -*-


class Solution(object):
    def maxProfit(self, k, prices):
        if not prices or k == 0:
            return 0

        # There is no limit on transaction's times in fact.
        days_num = len(prices)
        if k / 2 > days_num:
            return self.quick_solve(prices)

        # dp[i][j] is the max profit for up to i transactions by days j.
        # 1 <= i <= K, 0 <= j < das_num.
        dp = [[0 for day in range(days_num)] for trans in range(k + 1)]
        for i in range(1, k + 1):
            # tmpMax means the maximum profit if we've just buy i-th stock so far.
            tmp_max = -prices[0]
            for j in range(1, days_num):
                dp[i][j] = max(dp[i][j - 1], prices[j] + tmp_max)
                tmp_max = max(tmp_max, dp[i - 1][j - 1] - prices[j])
        return dp[k][days_num - 1]

    # Get the max profits without the limit of transactions actually.
    def quick_solve(self, prices):
        profits = 0
        for i in range(1, len(prices)):
            price_diff = prices[i] - prices[i - 1]
            profits += price_diff if price_diff > 0 else 0
        return profits

"""
1
[8,5,3]
2
[1,8,3,2,7,12,7,15,16,17]
4
[1,8,3,2,7,12,7,15,16,17]
"""
