#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 13:50:19 2020

@author: vanish
"""

from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # list is sorted in ascending order
        head = 0
        tail = len(numbers) - 1
        while head != tail:
            mysum = numbers[head] + numbers[tail]
            if (mysum == target):
                return [head+1, tail+1]
            else:
                if (mysum < target):
                    head += 1
                elif (mysum > target):
                    tail -= 1
                    
#%%
numbers = [-1,0]
target = -1
ans = Solution()
print (ans.twoSum(numbers, target))

