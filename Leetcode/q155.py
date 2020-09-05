#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 09:11:11 2020

@author: vanish
"""

#%%
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = list()
        self.top_ptr = -1
        self.minimum = None
        
    def push(self, x: int) -> None:
        self.top_ptr += 1
        if not self.data:
            curr_min = x
        else:
            curr_min = self.data[-1][1]
        self.data.append((x, min(curr_min, x)))
        
    def pop(self) -> None:
       del self.data[self.top_ptr]
       self.top_ptr -= 1

    def top(self) -> int:
        return self.data[self.top_ptr][0]
        
    def getMin(self) -> int:
        return self.data[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


#%%
obj = MinStack()
obj.push(1)
obj.pop()
obj.push(2)
obj.push(-7)
obj.push(-1)
obj.push(4)
param_3 = obj.top()
param_4 = obj.getMin()
