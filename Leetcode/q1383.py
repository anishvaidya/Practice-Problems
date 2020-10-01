#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 15:19:03 2020

@author: vanish
"""
from typing import List
import heapq
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        h = []
        sp_sum = 0
        ans = 0
        engineers = sorted(zip(efficiency, speed), reverse=True)
        print (engineers)
        for e in engineers:  
            heapq.heappush(h, e[1])
            sp_sum += e[1]
            if len(h) > k:
                less_sp = heapq.heappop(h)
                sp_sum -= less_sp
            ans = max(ans, sp_sum * e[0])
        return ans % (10 ** 9 + 7)
        
#%%
speed = [2,10,3,1,5,8]
efficiency = [5,4,3,9,7,2]
k = 2
ans = Solution()
print (ans.maxPerformance(len(speed), speed, efficiency, k))

# ans = sorted(zip(efficiency, speed), reverse=True)
# h = []
# import heapq

# heapq.heappush(h, 1)
# heapq.heappush(h, 0)