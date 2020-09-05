#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 11:57:06 2020

if nums[right] > (current_sum + nums[right]):
                max_sum = nums[right]
                current_sum = nums[right]
                left = right
                right += 1
                current_sum += nums[right]
                
            else:
                current_sum += nums[right]
                if current_sum > max_sum:
                    max_sum = current_sum
                    if nums[left] < 0:
                        current_sum -= nums[left]
                    else:
                        current_sum -= nums[left]
                    left += 1
                else:
                    right += 1


@author: vanish
"""
from typing import List
#%%
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]
        max_sum = nums[0]
        
        for num in nums[1:]:
            current_sum = max(current_sum + num, num)
            max_sum = max(max_sum, current_sum)
            
        return max_sum
    
#%%
nums = [-2,1,-3,4,-1,2,1,-5,4]
ans = Solution()
print (ans.maxSubArray(nums))
