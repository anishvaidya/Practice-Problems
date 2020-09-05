#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 08:02:37 2020

@author: vanish
"""

#%%
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 0 or num == 1:
            return True
        upper = num
        lower = 1
        while upper >= lower:
            middle = (upper + lower) // 2
            if middle ** 2 < num:
                lower = middle + 1
                root = middle
            elif middle ** 2 > num:
                upper = middle - 1
            else:
                return True
        return False

#%%
ans = Solution()
print (ans.isPerfectSquare(64))