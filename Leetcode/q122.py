#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 09:32:32 2020

@author: vanish
"""
from typing import List
#%%
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(1, len(prices)):
            max_profit += max(0, prices[i] - prices[i - 1])
        return max_profit
            
        
#%%
ans = Solution()
prices = [7,1,5,3,6,4]
print (ans.maxProfit(prices))          