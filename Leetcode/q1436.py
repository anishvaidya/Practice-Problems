#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 08:29:09 2020

@author: vanish
"""
from typing import List

#%%
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        destination = None
        '''
        cities = dict()
        for path in paths:
            cities[path[0]] = 1
            cities[path[1]] = cities.get(path[1], 0)
        for city in cities.keys():
            if cities[city] == 0:
                destination = city
        return destination
        '''
        destinations = set()
        sources = set()
        for path in paths:
            sources.add(path[0])
            destinations.add(path[1])
        destination = destinations.difference(sources)
        return destination.pop()
#%%
paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"], ["Mumbai", "London"]]
ans = Solution()
print (ans.destCity(paths))      