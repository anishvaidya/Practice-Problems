#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 11:38:29 2020

@author: vanish
"""

from typing import List
#%%
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_dict = dict()
        threshold = len(nums) // 2
        for num in nums:
            count_dict[num] = count_dict.get(num, 0) + 1
            if count_dict[num] > threshold:
                return num
        