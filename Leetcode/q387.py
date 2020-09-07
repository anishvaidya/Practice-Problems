#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 11:20:30 2020

@author: vanish
"""

#%%
class Solution:
    def firstUniqChar(self, s: str) -> int:
       seen = dict()
       for c in s:
           seen[c] = seen.get(c, 0) + 1
       for i,c in enumerate(s):
           if seen[c] == 1:
               return i
       return -1
   
#%%
s = "leetcode"
ans = Solution()
print (ans.firstUniqChar(s))
               