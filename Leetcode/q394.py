#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 09:37:14 2020

@author: vanish
"""
# Input: s = "3[a2[c]]"
# Output: "accaccacc"
#%%
class Solution:
    def decodeString(self, s: str) -> str:
        char_stack = []
        num_stack = []
        i = 0
        ans = ""
        while i < len(s):
            print (char_stack)
            print (num_stack)
            print (ans)
            if s[i].isdigit():
                number = 0
                while s[i].isdigit():
                    number = number * 10 + int(s[i])
                    i += 1
                num_stack.append(number)
            elif s[i] == "[":
                char_stack.append(ans)
                ans = ""
                i += 1
            elif s[i].isalpha():
                ans += s[i]
                i += 1
            elif s[i] == "]":
                string = char_stack.pop()
                count = num_stack.pop()
                decoded = string + count * ans
                ans = decoded
                i += 1
        return ans
    
#%%
ans = Solution()
print (ans.decodeString("3[a2[c]]"))
                