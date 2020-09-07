#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 16:29:00 2020

@author: vanish
"""

from typing import List
#%%
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count_dict = dict()
        for num in nums:
            count_dict[num] = count_dict.get(num, 0) + 1
        for num in count_dict.keys():
            if count_dict[num] == 1:
                return num