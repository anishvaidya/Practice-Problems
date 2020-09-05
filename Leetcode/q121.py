#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 09:22:28 2020

@author: vanish
"""

from typing import List
#%%
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')
        for price in prices:
            min_price = min(price, min_price)
            profit = price - min_price
            max_profit = max(profit, max_profit)
        return max_profit
        
#%%
ans = Solution()
prices = [7,6,4,3,1]
print (ans.maxProfit(prices))        