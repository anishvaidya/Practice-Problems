#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 13:02:28 2020

@author: vanish
"""

#%%
class Solution:
    def titleToNumber(self, s: str) -> int:
        length = len(s)
        answer = 0
        for i in range(length):
            answer += (ord(s[i]) - 64) * (26 ** (length - i - 1))
        return answer
    
#%%
ans = Solution()
print (ans.titleToNumber("ZZ"))
        
        