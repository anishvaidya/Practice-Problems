#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 16:12:32 2020

@author: vanish
"""

from typing import List
#%%
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count_dict = dict()
        ans = list()
        top_k = list()
        for word in words:
            count_dict[word] = count_dict.get(word, 0) + 1
        ans = sorted(count_dict.items(), key = lambda x: (-x[1],x[0]))
        for i in range(k):
            top_k.append(ans[i][0])
        return top_k
    
#%%

