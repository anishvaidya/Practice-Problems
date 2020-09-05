#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 07:36:53 2020

@author: vanish
"""

#%%
class Solution:
    def mySqrt(self, x: int) -> int:
        '''
        ans = 0
        while (ans ** 2 <= x):
            ans += 1
        return ans - 1
        '''
        if x == 0 or x == 1:
            return x
        upper = x
        lower = 1
        while upper >= lower:
            middle = (upper + lower) // 2
            if middle ** 2 < x:
                lower = middle + 1
                root = middle
            elif middle ** 2 > x:
                upper = middle - 1
            else:
                root = middle
                return root
        return root
            
    
#%%
ans = Solution()
print (ans.mySqrt(5))