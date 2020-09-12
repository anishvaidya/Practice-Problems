#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 12:07:34 2020

@author: vanish
"""
from typing import List
#%%
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        threshold = len(nums) // 3
        majority_list = list()
        ans1 = None
        ans2 = None
        count1 = 0
        count2 = 0
        for num in nums:
            if num == ans1:
                count1 += 1
            elif num == ans2:
                count2 += 1
            elif count1 == 0:
                ans1 = num
                count1 += 1
            elif count2 == 0:
                ans2 = num
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        if nums.count(ans1) > threshold:
            majority_list.append(ans1)
        if nums.count(ans2) > threshold:
            majority_list.append(ans2)
        return majority_list
            
    
#%%
nums = [1,1,1,3,3,2,2,2]
ans = Solution()
print (ans.majorityElement(nums))