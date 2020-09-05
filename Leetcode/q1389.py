#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 15:42:08 2020

@author: vanish
"""
from typing import List
#%%
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        answer = list()
        for i in range(len(index)):
            if index[i] == len(answer):
                answer.append(nums[i])
            else:
                answer = answer[:index[i]] + [nums[i]] + answer[index[i]:]
                
        return answer
    
#%%

nums = [0,1,2,3,4]
index = [0,1,2,2,1]
ans = Solution()
print (ans.createTargetArray(nums, index))