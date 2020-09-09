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
        '''
        # Space complexity: O(n)
        pending = set()
        for i in range(1, len(nums) + 1):
            pending.add(i)
        for num in nums:
            if num in pending:
                pending.remove(num)
        return list(pending)
        '''
        # Space complexity: O(1)
        missing = list()
        for num in nums:
            index = abs(num) - 1
            nums[index] = -1 * (abs(nums[index]))
        for index, num in enumerate(nums):
            if num > 0:
                missing.append(index + 1)
        return missing
        
#%%
nums = [4,3,2,7,8,2,3,1]
ans = Solution()
print (ans.findDisappearedNumbers(nums))