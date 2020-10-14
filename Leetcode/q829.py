#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 10:29:49 2020

@author: vanish
"""

'''
N can be expressed as k, k + 1, k + 2, ..., k + (i - 1), where k is a positive integer; therefore

N = k * i + (i - 1) * i / 2 => N - (i - 1) * i / 2 = k * i, which implies that as long as N - (i - 1) * i / 2 is k times of i, we get a solution corresponding to i; Hence iteration of all possible values of i, starting from 1, will cover all cases of the problem.
'''

class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        ans = 0
        i = 1
        while N > ((i - 1) * i // 2):
            if (N - ((i - 1) * i // 2)) % i == 0:
                ans += 1
            i += 1
        return ans

#%% 
N = 1
ans = Solution()
print (ans.consecutiveNumbersSum(N))