#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 09:37:14 2020

@author: vanish
"""

#%%
class Solution:
    def decodeString(self, s: str) -> str:
        ans = ""
        stack = ""
        bracket = 0
        count = ""
        for c in s[::-1]:
            if c == "]":
                bracket += 1
            elif c.isalpha() and bracket:
                stack += c
            elif c == "[":
                bracket -= 1
            elif c.isnumeric():
                count += c