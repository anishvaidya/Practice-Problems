#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 13:37:40 2020

@author: vanish
"""

#%%
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        addition = ""
        len_a = len(a)
        len_b = len(b)
        if len_a > len_b:
            length = len_a
        else:
            length = len_b
        for i in range(1, length + 1):
            try:
                a_i = int(a[-i])
            except (IndexError, ValueError):
                a_i = 0
            try:
                b_i = int(b[-i])
            except (IndexError, ValueError):
                b_i = 0
            if i == 1:
                add_bit = a_i or b_i
                carry = a_i and b_i
                if carry:
                    add_bit = 0
                addition = str(add_bit) + addition
            else:
                add_bit = a_i or b_i or int(carry)
                all_true = a_i and b_i and int(carry)
                carry = (a_i and b_i) or (b_i and int(carry)) or (a_i and int(carry))
                
                if carry and not all_true:
                    add_bit = 0
                addition = str(add_bit) + addition
        if carry:
            addition = str(carry) + addition
        return addition
    
#%%

ans = Solution()
print (ans.addBinary("1100", "110"))