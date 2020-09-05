#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 12:22:32 2020

@author: vanish
"""

#%%
class Solution:
    def convertToTitle(self, n: int) -> str:
        answer = ""
        if n <= 26:
            return chr(64 + n)
        quotient = n // 26
        remainder = n % 26
        if quotient == 0:
            answer = chr(64 + remainder)
        else:
            answer = self.convertToTitle(quotient) + chr(64 + remainder)
        if remainder == 0:
            answer = self.convertToTitle(quotient - 1) + chr(64 + 26)
        return answer

#%%
ans = Solution()
print (ans.convertToTitle(18278))