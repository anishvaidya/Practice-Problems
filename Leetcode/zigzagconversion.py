#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 10:40:03 2019

@author: vanish
"""
#%%
def convert(s: str, numRows: int) -> str:
        list_s = list(s)
        solution = []
        for char in list_s:
            
            for i in range(numRows):
                row = []
                row.append(list_s[i])
                solution.append(row)
                
                list_s.remove(list_s[0])
#            print (row)
            
        
        return solution    
convert('paypalishiring', 3)           
            
        
#%%