#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 16:00:48 2020

@author: vanish
"""
from typing import List
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if len(matrix) == 0:
            return
        self.dp = [[0 for j in range(len(matrix[0]) + 1)] for i in range(len(matrix) + 1)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.dp[i + 1][j + 1] = self.dp[i + 1][j] + self.dp[i][j + 1] + matrix[i][j] - self.dp[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        answer = self.dp[row2 + 1][col2 + 1] - self.dp[row2 + 1][col1] - self.dp[row1][col2 + 1] + self.dp[row1][col1]
        return answer


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)