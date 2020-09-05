#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 12:33:15 2020

@author: vanish
"""
from typing import List
from collections import deque
#%%
class Solution:
    def addToArrayForm(self, digits: List[int], K: int) -> List[int]:
        answer = deque()
        carry = 0
        inserted = 0
        for i in range(len(digits) - 1, -1, -1):
            addition = digits[i] + (K % 10) + carry
            K = K // 10
            if (addition < 10):
                answer.appendleft(addition)
                carry = 0
            else:
                answer.appendleft(addition % 10)
                carry = addition // 10
                if i == 0:
                    # answer.appendleft(1)
                    inserted = 1
        
        if K or inserted:
            K = K + inserted
            if K >= 10:
                while K > 0:
                    answer.appendleft(K % 10)
                    K = K // 10
            else:
                answer.appendleft(K)
            
        return list(answer)
    
#%%
digits = [4,9]
ans = Solution()
myans = (ans.addToArrayForm(digits, 983))
