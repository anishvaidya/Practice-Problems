#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 11:33:27 2020

@author: vanish
"""

from typing import List
#%%
class Solution:
    def search_left(self, nums, target):
        left = -1
        low = 0
        high = len(nums) - 1
        while low <= high:
            # mid = (low + high) // 2
            mid = low + (high - low) // 2
            if target > nums[mid]:
                low = mid + 1
            elif target <= nums[mid]:
                high = mid - 1
            if target == nums[mid]:
                left = mid
        return left
    
    def search_right(self, nums, target):
        right = -1
        low = 0
        high = len(nums) - 1
        while low <= high:
            # mid = (low + high) // 2
            mid = low + (high - low) // 2
            if target >= nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high = mid - 1
            if target == nums[mid]:
                right = mid
        return right
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.search_left(nums, target)
        right = self.search_right(nums, target)
        return [left, right]
        
#%%
nums = [1,1,2,2,2,2,2,3,4,5,6,7,8,89]
target = 2
ans = Solution()
print (ans.searchRange(nums, target))
