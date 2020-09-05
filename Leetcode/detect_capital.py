#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 15:59:11 2020

@author: vanish
"""
# Detect capital
# better choice - use isUpper()
# better choice - break in between if string is AnIsh
#%%
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        isFirstCapital = False
        capital_count = 0 
        for i in range(len(word)):
            if i == 0:
                if word[i] >= 'A' and word[i] <= 'Z':
                    isFirstCapital = True
                    capital_count += 1
            else:
                if word[i] >= 'A' and word[i] <= 'Z':
                    capital_count += 1
        if (not isFirstCapital):
            if capital_count == 0:
                return True
            else:
                return False
        elif isFirstCapital:
            if (capital_count == 1) or (capital_count == len(word)):
                return True
            else:
                return False
        
#%%        
ans = Solution()
word = "vAidya"
print (ans.detectCapitalUse(word))