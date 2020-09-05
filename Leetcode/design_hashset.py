#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 16:18:32 2020

@author: vanish
"""

# design hashset
#%% 
class Bucket:
    def __init__(self):
        self.bucket = list()
    
    def add(self, value: int) -> None:
        isPresent = False
        for i, k in enumerate(self.bucket):
            if value == k:
                isPresent = True
                break
        if not isPresent:
            self.bucket.append(value)
    
    def get(self, value: int) -> bool:
        isPresent = False
        for num in self.bucket:
            if num == value:
                isPresent = True
                break
        return isPresent
    
    def remove(self, value: int) -> None:
        for i, k in enumerate(self.bucket):
            if k == value:
                del self.bucket[i]
                break
        
#%%
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.n_bucket = 1024
        self.hashset = [Bucket() for i in range(self.n_bucket)]
        
    def add(self, key: int) -> None:
        self.hashset[key % self.n_bucket].add(key)
        

    def remove(self, key: int) -> None:
        self.hashset[key % self.n_bucket].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        isPresent = self.hashset[key % self.n_bucket].get(key)
        return isPresent
        

#%%
# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
obj.add(1)
obj.remove(1)
obj.add(2)
obj.add(1025)
obj.remove(2049)
obj.add(2049)
param_3 = obj.contains(2049)