#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 11:39:16 2020

@author: vanish
"""

from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = list()
        intervals.sort(key = lambda x: x[0])
        for interval in intervals:
            if len(merged) == 0:
                merged.append(interval)
            elif merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                if merged[-1][1] < interval[1]:
                    merged[-1][1] = interval[1]
        return merged

#%%
intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals = [[1,4],[2,3]]
ans = Solution()
print (ans.merge(intervals))