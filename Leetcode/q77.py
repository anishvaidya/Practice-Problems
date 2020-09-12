#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 12:32:03 2020

@author: vanish
"""

#%%
from typing import List
from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list()
        for i in range(n):
            nums.append(i+1)
        answer = list(combinations(nums, k))
        return answer