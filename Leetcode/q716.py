#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 12:30:19 2020

@author: vanish
"""

#%%
class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = list()
        self.max_stack = list()
        self.sec_stack = list()
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        if (len(self.max_stack) == 0 or x >= self.max_stack[-1]):
            self.max_stack.append(x)
        

    def pop(self) -> int:
        popped = self.stack.pop()
        if popped == self.max_stack[-1]:
            self.max_stack.pop()
        return popped

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return self.max_stack[-1]

    def popMax(self) -> int:
        curr_max = self.max_stack.pop()
        while self.stack[-1] != curr_max:
            self.sec_stack.append(self.stack.pop())
        popped_max = self.stack.pop()
        while self.sec_stack:
            self.push(self.sec_stack.pop())
            
        return popped_max
        
#%%

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()