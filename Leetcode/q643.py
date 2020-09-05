#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 10:29:16 2020

@author: vanish
"""

from typing import List
#%%
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = float("-inf")
        curr_sum = 0
        '''
        for j in range(k):
            curr_sum += nums[j]
        '''
        curr_sum = sum(nums[:k])
        max_avg = max(max_avg, curr_sum)
        for i in range(1, len(nums) - k + 1):
            curr_sum += -nums[i - 1] + nums[i + k - 1]
            max_avg = max(max_avg, curr_sum)
        '''i = 1
        while i < (len(nums) - k + 1):
            curr_sum -= nums[i - 1]
            curr_sum += nums[i + k - 1]
            max_avg = max(max_avg, curr_sum)
            i += 1
        '''
        return (max_avg / k)
    
#%%
nums = [1,12,3, -5, 7, 8, 10, 15]
k = 4
ans = Solution()
print (ans.findMaxAverage(nums, k))
