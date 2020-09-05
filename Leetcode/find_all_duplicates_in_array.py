#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 10:05:44 2020

@author: vanish
"""

from typing import List
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        twice = list()
        count_dict = dict()
        for num in nums:
            if num in count_dict:
                count_dict[num] += 1
            else: count_dict[num] = 1
            if count_dict[num] >= 2:
                twice.append(num)
        return twice