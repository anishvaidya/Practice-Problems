#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 18:46:08 2020

@author: vanish
"""

from typing import List
class Solution:
    # n ** 2
    def trap(self, height: List[int]) -> int:
        ans = 0
        
        for i in range(len(height)):
            left_max = 0
            right_max = 0
            if i == 0:
                left_max = 0
            else:
                left_max = max(height[:i])
            if i == len(height) - 1:
                right_max = 0
            else:
                right_max = max(height[i+1:])
            print (left_max, right_max)
            ans += min(left_max, right_max) - height[i]
            print (ans)
        return ans
        
        

#%%
height = [0,1,0,2,1,0,1,3,2,1,2,1]
expected = 6


ans = Solution()
print (ans.trap(height))
