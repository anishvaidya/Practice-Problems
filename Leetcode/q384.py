#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 11:06:29 2020

@author: vanish
"""
import random
from typing import List

#%%
class Solution:

    def __init__(self, nums: List[int]):
        self.my_list = nums
        self.original = list(nums)

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.my_list = self.original
        self.original = list(self.original)
        return self.original
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        for i in range(len(self.my_list)):
            index = random.randint(i, len(self.my_list) - 1)
            self.my_list[index], self.my_list[i] = self.my_list[i], self.my_list[index]
        return self.my_list
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
#%%
nums = [1, 12, 3, -5, 7, 8, 10, 15]
obj = Solution(nums)
param_1 = obj.reset()
param_2 = obj.shuffle()