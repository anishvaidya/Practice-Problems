#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 11:01:57 2020

@author: vanish
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # timeout
        # i = 0
        # if not haystack and not needle:
        #     return 0
        # while i < len(haystack):
        #     t = i
        #     j = 0
        #     while j < len(needle) and t < len(haystack) and needle[j] == haystack[t]:
        #         t += 1
        #         j += 1
        #     if j == len(needle):
        #         return i
        #     i += 1
        # return -1
        for i in range(len(haystack) - len(needle) + 1):
            if needle == haystack[i:i + len(needle)]:
                return i
        return -1