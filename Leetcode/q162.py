#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 18:35:12 2020

@author: vanish
"""

from typing import List
#%%
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) > 1:
            if nums[0] > nums[1]:
                return 0
            if nums[len(nums) - 1] > nums[len(nums) - 2]:
                return len(nums) - 1
        for i in range(1, len(nums) - 1):
            if nums[i] > nums[i -1] and nums[i] > nums[i + 1]:
                return i
        return -1

#%%
nums = [1,2,3,1]
ans = Solution()
print (ans.findPeakElement(nums))
            