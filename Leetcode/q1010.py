#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 16:12:02 2020

@author: vanish
"""

from typing import List
from math import comb
#%%
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        answer = 0
        check_array = [0] * 60
        for i in time:
            rem = i % 60
            check_array[rem] += 1
        for i in range(len(check_array) // 2):
            if i == 0:
                answer += comb(check_array[i], 2)
            else:
                answer += check_array[i] * check_array[60 - i]
        if check_array[30] > 2:
            answer += comb(check_array[30], 2)
        elif check_array[30] == 2:
            answer += 1
        return answer

#%%
time = [30,20,150,100,40]
time = [418,204,77,278,239,457,284,263,372,279,476,416,360,18]
# time = [60,60,60]
# time = [439,407,197,191,291,486,30,307,11]
ans = Solution()
print (ans.numPairsDivisibleBy60(time))