#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 14:43:08 2020

@author: vanish
"""

from typing import List
#%%
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        backup = list()
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                backup.append(nums.pop(i))
                i -= 1
            i += 1
        nums.extend(backup)

#%%
nums = [0,1,0,3,12]
# nums = [0,0,1]
ans = Solution()
ans.moveZeroes(nums)
        