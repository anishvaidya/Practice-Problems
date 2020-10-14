#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 19:00:50 2020

@author: vanish
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if len(coins) == 0 or amount < 0:
            return -1
        dp = [(amount + 1) for i in range(amount + 1)]
        dp[0] = 0
        
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        if dp[-1] != (amount + 1):
            return dp[-1]
        else:
            return -1