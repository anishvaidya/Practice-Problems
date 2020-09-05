#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 15:20:31 2020

@author: vanish
"""
from typing import List
#%%
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        decompressed = list()
        i = 0
        check = 2 * i + 1
        while (check <= len(nums)):
            freq = nums[2 * i]
            val = nums[2 * i + 1]
            for j in range(freq):
                decompressed.append(val)
            i += 1
            check = 2 * i + 1
        return decompressed
    
#%%
nums = [65,44,72,15]
ans = Solution()
print (ans.decompressRLElist(nums))