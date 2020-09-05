#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 09:04:17 2020

@author: vanish
"""

#%%
class Solution:
    def reverseWords(self, s: str) -> str:
        reversed_string = ""
        word_list = list()
        word = ""
        for i in s:
            if i == " ":
                if word != "":
                    word_list.append(word)
                word = ""
                continue
            word += i
        if word:
            word_list.append(word)
        if len(word_list) == 0:
            return ""
        for i in range(len(word_list) - 1, 0, -1):
            reversed_string += word_list[i] + " "
        reversed_string += word_list[0]
        return reversed_string
        
#%%

ans = Solution()
s = "the sky is blue"
print (ans.reverseWords(s))
            