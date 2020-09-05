#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 23:00:56 2020

@author: vanish
"""

from typing import List
#%%
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        '''
        answer = [-1] * len(A)
        even = 0
        odd = 1
        for num in A:
            if (num % 2 == 0):
                answer[even] = num
                even += 2
            else:
                answer[odd] = num
                odd += 2
        return answer
        '''
        
        
    
        
    
#%%
A = [4,2,5,7]
ans = Solution()
print (ans.sortArrayByParityII(A))

        
