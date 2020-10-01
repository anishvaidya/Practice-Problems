#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 14:05:51 2020

@author: vanish
"""

from typing import List
class Solution:
    def twoSumPtr(self, nums, i, ans):
        i = i
        lo = i + 1
        high = len(nums) - 1
        while lo < high:
            mysum = nums[i] + nums[lo] + nums[high]
            if mysum == 0:
                ans.append([nums[i], nums[lo], nums[high]])
                lo += 1
                high -= 1
                while lo < high and nums[lo] == nums[lo - 1]:
                    lo += 1
            elif mysum > 0:
                high -= 1
            elif mysum < 0:
                lo += 1
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i-1] != nums[i]:
                self.twoSumPtr(nums, i, ans)
        return ans
    
#%%
nums = [-1,0,1,2,-1,-4]
ans = Solution()
print (ans.threeSum(nums))