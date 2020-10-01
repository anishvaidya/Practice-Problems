#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 10:51:40 2020

@author: vanish
"""
# Input: s = "deeedbbcccbdaa", k = 3
# Output: "aa"
#%%
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        count = [0] * len(s)
        i = 1
        count[0] =1 
        while i < len(s):

            if s[i] != s[i - 1]:
                count[i] = 1
            elif s[i] == s[i - 1]:
                count[i] = count[i - 1] + 1
                if count[i] == k:
                    # for a in range(k):
                    s = s[:i-k+1] + s[i+1:]
                    count = count[:i-k+1] + count[i+1:]
                    i -= k
            i += 1
        return s

#%%
s = "deeedbbcccbdaa"
k = 3
s = "pbbcggttciiippooaais"
k = 2
ans = Solution()
print (ans.removeDuplicates(s, k))