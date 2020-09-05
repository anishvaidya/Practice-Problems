#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 11:21:20 2020

@author: vanish
"""
from typing import List
#%%
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = False
        for i in range(len(digits) - 1, -1, -1):
            incr = digits[i] + 1
            if incr < 10:
                digits[i] = incr
                carry = False
                break
            else:
                digits[i] = 0
                carry = True
        if carry:
            digits.insert(0, 1)
        return digits
        
        
#%%
digits = [8,9,9,9]
ans = Solution()
print (ans.plusOne(digits))