#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    """ As long as there is a price gap, we gain a profit.
    """
    def maxProfit(self, prices):
        max_profit = 0
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i - 1]
            if diff > 0:
                max_profit += diff
        return max_profit

"""
[]
[3,4,5,6,2,4]
[6,5,4,3,2,1]
[1,2,3,4,3,2,1,9,11,2,20]
"""
