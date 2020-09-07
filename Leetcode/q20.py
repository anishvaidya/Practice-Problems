#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 16:33:32 2020

@author: vanish
"""

#%%
class Solution:
    def isValid(self, s: str) -> bool:
        if (len(s) % 2):
            return False
        balanced_count = 0
        stack = list()
        pair = {")": "(",
                "}": "{",
                "]": "["}
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
                balanced_count += 1
            else:
                if len(stack) != 0:
                    if pair[char] != stack.pop():
                        return False
                    else:
                        balanced_count -= 1
                else:
                    return False
        if not balanced_count:
            return True
        else:
            return False
    
#%%
# s = "()[]{}"
s = "()]"
ans = Solution()
print (ans.isValid(s))