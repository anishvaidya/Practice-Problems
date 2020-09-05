#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 08:12:14 2020

@author: vanish
"""

#%%
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 0:
            return 0
        length = 0
        i = 1
        character = s[-1]
        while (character == " "):
            i += 1
            try:
                character = s[-i]
            except (ValueError, IndexError):
                return 0
        
        while (character != " "):
            length += 1
            i += 1
            try:
                character = s[-i]
            except (ValueError, IndexError):
                character = " "
        return length

#%%
ans = Solution()
print (ans.lengthOfLastWord(" "))