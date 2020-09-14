#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 14:48:12 2020

@author: vanish
"""

from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        from itertools import combinations
        power_set = list()
        for i in range(0, len(nums) + 1):
            combs = list(combinations(nums, i))
            power_set.extend(combs)
        return power_set
        