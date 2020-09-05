#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 14:51:24 2020

@author: vanish
"""
            
#%%    
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        is_negative = False
        if (dividend ^ divisor < 0):
            is_negative = True   
        if dividend < 0:
                dividend = ~(dividend) + 1
        if divisor < 0:
            divisor = ~(divisor) + 1
        quotient = 0
        while (dividend - divisor >= 0):
            shift_count = 0
            while (dividend - (divisor<<1<<shift_count) >= 0):
                shift_count += 1
            quotient += 1<<shift_count
            dividend = dividend - (divisor<<shift_count)
        if is_negative:
            quotient = ~(quotient) + 1
        return min(max(-2 ** 31, quotient), 2 ** 31 -1)
        
                
                
#%%        
ans = Solution()
print (ans.divide(-3, -3))