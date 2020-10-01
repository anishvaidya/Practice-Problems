#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 15:46:02 2020

@author: vanish
"""

from typing import List
from queue import deque
class Solution:
    def cleanQ(self, nums, k):
    
    
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # timeout
        # dq = deque()
        # max_list = []
        # for i in range(k):
        #     dq.append(nums[i])
        # max_list.append(max(dq))
        # for i in range(k, len(nums)):
        #     if len(dq) == k:
        #         dq.popleft()
        #     dq.append(nums[i])
        #     max_list.append(max(dq))
        # return max_list
    
        # optimized
        dq = deque()
        max_list = []
        curr_max = float("-inf")
        for i in range(k):
            curr_max = max(curr_max, nums[i])
            dq.append(i)
        max_list.append(curr_max)
        print (dq)
        return max_list
        
        
#%%
nums = [1,3,-1,-3,5,3,6,7]
k = 3

ans = Solution()
print (ans.maxSlidingWindow(nums, k))