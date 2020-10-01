#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 16:20:40 2020

@author: vanish
"""

from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s = Counter(s)
        count_t = Counter(t)
        # convert t to s
        print (count_s-count_t)
        difference = (count_s - count_t).values()
        return sum(difference)
    
    
    
dict1 = Counter({'e': 3, 'l': 1, 't': 1, 'c': 1, 'o': 1, 'd': 1})
dict2 = Counter({'c': 2, 'p': 1, 'r': 1, 'a': 1, 't': 1, 'i': 1, 'e': 1})

