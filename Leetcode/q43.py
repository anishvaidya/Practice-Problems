#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 11:42:42 2020

@author: vanish
"""

#%%
class Solution:
    def get_int(self, number: str) -> int:
        integer = 0
        for i in range(len(number) - 1, -1, -1):
            integer += (ord(number[i]) - ord('0')) * 10 ** (len(number) -1 - i)
        return integer
        
    
    def multiply(self, num1: str, num2: str) -> str:
        number1 = self.get_int(num1)
        number2 = self.get_int(num2)
        product = number1 * number2
        answer = ""
        if product == 0:
            return "0"
        while product > 0:
            answer = (chr(ord('0') + product % 10)) + answer
            product = product // 10
        return answer
    
#%%
ans = Solution()
myans = (ans.multiply("50", "0"))
