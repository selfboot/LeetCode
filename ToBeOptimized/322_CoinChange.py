#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuezaigds@gmail.com
# Can also be solved with branch and bound, beaten 99% python submissions
# Refer to:
# https://leetcode.com/discuss/79289/fast-python-branch-bound-solution-beaten-python-submissions

class Solution(object):
    def coinChange(self, coins, amount):
        """
        Very classic dynamic programming problem, like 0-1 Knapsack problem.
        dp[i] is the fewest number of coins making up amount i,
        then for every coin in coins, dp[i] = min(dp[i - coin] + 1).
        """
        dp = [amount + 1] * (amount+1)
        dp[0] = 0
        for i in xrange(amount+1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        return -1 if dp[amount] > amount else dp[amount]


class Solution_2(object):
    def coinChange(self, coins, amount):
        # BFS Way.  Scan the possible tree level by level. More Faster!
        if amount == 0:
            return 0
        amounts = [False] * (amount + 1)
        coins_sum = [0]
        count = 0

        # upper bound on number of coins (+1 to represent the impossible case)
        coins.sort(reverse = True)
        upperBound = amount / coins[-1] + 1

        # Use upperBound to pruning.
        while coins_sum and count < upperBound:
            new_coins_sum = []
            count += 1
            for s in coins_sum:
                for coin in coins:
                    new_sum = s + coin
                    if new_sum == amount:
                        return count
                    elif new_sum > amount:
                        continue
                    elif not amounts[new_sum]:
                        amounts[new_sum] = True
                        new_coins_sum.append(new_sum)
                    else:
                        pass
            coins_sum = new_coins_sum
        return -1

"""
[1, 2, 5]
11
[1]
0
[2]
3
"""
