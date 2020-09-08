#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 23:42:10 2020

@author: vanish
"""
from typing import List
#%%
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # pending = set([i for i in range(1, len(nums) + 1)])
        pending = set()
        for i in range(1, len(nums) + 1):
            pending.add(i)
        for num in nums:
            if num in pending:
                pending.remove(num)
        return list(pending)
        
        
#%%
nums = [4,3,2,7,8,2,3,1]
ans = Solution()
print (ans.findDisappearedNumbers(nums))