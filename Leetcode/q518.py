#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 19:01:05 2020

@author: vanish
"""

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for i in range(amount+1)]
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = dp[i] + dp[i-coin]
        return dp[-1]