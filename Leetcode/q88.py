#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 10:36:47 2020

@author: vanish
"""
from typing import List
#%%
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m != 0 and n != 0:
            if nums1[m - 1] < nums2[n - 1]:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
            else:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
        if n != 0:
            nums1[: n] = nums2[: n]
                
#%%
nums1 = [10,101,200,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
#%%
ans = Solution()
print (ans.merge(nums1, m, nums2, n))

                
        