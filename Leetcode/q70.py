#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 07:44:18 2020

@author: vanish
"""

#%%
class Solution:
    def climbStairs(self, n: int) -> int:
        # if n == 2:
        #     return 2
        # if n == 1:
        #     return 1
        # if n <= 0:
        #     return 0
        # else:
        #     return self.climbStairs(n-1) + self.climbStairs(n - 2)
        if n == 0 or n == 1:
            return 1
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
        
#%%
ans = Solution()
print (ans.climbStairs(38))
