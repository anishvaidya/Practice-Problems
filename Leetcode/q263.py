#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 13:40:09 2020

@author: vanish
"""

class Solution:
    def isPrime(self, i: int) -> bool:
        if i == 1:
            return False
        if i <= 3:
            return True
        for j in range(2, i // 2 + 1):
            if not (i % j):
                return False
        return True
    
    def isUgly(self, num: int) -> bool:
        while not (num % 2):
            num = num // 2
        print (num)
        for i in range(2, num + 1):
            # print (i)
            if not (num % i):
                # print (num % i)
                # print (self.isPrime(i))
                if self.isPrime(i):
                    if i == 2 or i == 3 or i == 5:
                        continue
                    else:
                        return False
        return True
    
#%%
ans = Solution()
num = 905391974
print (ans.isUgly(num))


