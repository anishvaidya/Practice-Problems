#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 17:12:36 2020

@author: vanish
"""
from typing import List
from functools import cmp_to_key
class Solution:
    def compare(self, log1, log2):
        id1 = log1.split(" ", 1)[0]
        id2 = log2.split(" ", 1)[0]
        cont1 = log1.split(" ", 1)[1]
        cont2 = log2.split(" ", 1)[1]
        
        if log1.split(" ", 1)[1].split(" ", 1)[0].isdigit():
            type1 = "dig"
        else: 
            type1 = "let"
            
        if log2.split(" ", 1)[1].split(" ", 1)[0].isdigit():
            type2 = "dig"
        else:
            type2 = "let"

        
        if type1 == type2 == "let":
            if cont1 < cont2:
                return -1
            elif cont1 > cont2:
                return 1
            else:
                if id1 <= id2:
                    return -1
                else:
                    return 1
        
        elif type1 == type2 == "dig":
            return 0
        elif type1 == "let" and type2 == "dig":
            return -1
        else:
            return 1
        
        
            
            
        
    
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        logs.sort(key=cmp_to_key(self.compare))
        return logs
        
#%%
logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]

# logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
# expected = ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]


ans = Solution()
print (ans.reorderLogFiles(logs))