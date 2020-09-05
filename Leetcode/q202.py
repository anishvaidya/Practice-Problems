#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 12:36:15 2020

@author: vanish
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        seen = set()
        while n != 1:
            indie = list()
            seen.add(n)
            while n:
                indie.append(n % 10)
                n = n // 10
            sq_sum = 0
            for digit in indie:
                sq_sum += digit ** 2
            n = sq_sum
            if n in seen:
                return False
        if n == 1:
            return True


#%%
ans = Solution()
n = 37
print (ans.isHappy(n))