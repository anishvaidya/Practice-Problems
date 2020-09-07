#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 15:15:10 2020

@author: vanish
"""

from typing import List
#%%
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = dict()
        ans = list()
        top_k = list()
        for num in nums:
            count_dict[num] = count_dict.get(num, 0) + 1
        ans = sorted(count_dict.items(), key = lambda x: x[1], reverse=True)
        for i in range(k):
            top_k.append(ans[i][0])
        return top_k
    
#%%
nums = [1,1,1,2,2,3]
k = 2
ans = Solution()
print (ans.topKFrequent(nums, k))