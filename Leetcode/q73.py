#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 15:34:11 2020

@author: vanish
"""

from typing import List
#%%
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        '''
        Space complexity: O(m + n)
        '''
        remove_row = set()
        remove_column = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    remove_row.add(i)
                    remove_column.add(j)
        for i in remove_row:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0
        for i in range(len(matrix)):
            for j in remove_column:
                matrix[i][j] = 0
        print (matrix)
        
        
        
#%%
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
ans = Solution()
ans.setZeroes(matrix)

                    