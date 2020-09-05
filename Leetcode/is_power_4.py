#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 15:13:24 2020

@author: vanish
"""

# Power of Four
#%%
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0:
            return False
        if num == 1:
            return True
        bin_num = bin(num)[2:]
        count_z = 0
        for i in range(1, len(bin_num)):
            if bin_num[i] == '1':
                return False
            else: 
                count_z += 1
        if count_z % 2:
            return False
        return True
            
#%%
ans = Solution()
num = 64
print (ans.isPowerOfFour(num))