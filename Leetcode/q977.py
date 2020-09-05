#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 08:59:04 2020

@author: vanish
"""

from typing import List
#%%
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        '''
        squares = list()
        for num in A:
            squares.append(num * num)
        squares = sorted(squares)
        return squares
        '''
        return sorted(map(lambda x: x * x, A))
    
#%%