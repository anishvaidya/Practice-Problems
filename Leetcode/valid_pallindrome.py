#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 16:57:13 2020

@author: vanish
"""

'''
Input: "A man, a plan, a canal: Panama"
Output: true

Input: "race a car"
Output: false
'''
# 1 2 3 4 5 6
#%%
class Solution:
    def isPalindrome(self, s: str) -> bool:
        pallindrome = True
        left = 0
        right = len(s) - 1
        if not len(s):
            return True
        while left <= right:
            while not s[left].isalnum() and left < right:
                left += 1
            while not s[right].isalnum() and left < right:
                right -= 1
            if s[left].lower() != s[right].lower():
                pallindrome = False
                break
            left += 1
            right -= 1
        return pallindrome
    
#%%
ans = Solution()
s = "A man, a plan, a canal: Panama"
# s = ",,,,,,,,,,,,acva"
print (ans.isPalindrome(s))