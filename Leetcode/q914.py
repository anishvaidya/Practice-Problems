#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 08:56:26 2020

@author: vanish
"""

from typing import List
from math import gcd
from functools import reduce
#%%
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) < 2:
            return False
        count_dict = dict()
        for num in deck:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1
        ''' #n*n solution
        min_count = min(count_dict.values())
        is_possible = False
        for size in range(2, min_count + 1):
            for key in count_dict:
                if count_dict[key] < 2:
                    return False
                if (count_dict[key] % size) == 0:
                    is_possible = True
                else:
                    is_possible = False
                    break
            if is_possible:
                return is_possible
        return False
        '''
        counts = count_dict.values()
        my_gcd = reduce(gcd, counts)
        if my_gcd >= 2:
            return True
        else:
            return False
        
        
#%%
deck = [1,2,3,4,4,3,2,1]
ans = Solution()
print (ans.hasGroupsSizeX(deck))
        