#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 14:12:15 2020

@author: vanish
"""
from typing import List
class Solution:
    
    def dfs(self, node, graph, path):
            target = len(graph)-1
            if node == target:
                return [path + [target]]
            res = []
            for child in graph[node]:
                curr = self.dfs(child, graph, path + [node])
                res = res + curr
            return res
    
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # self.graph = graph
        # if not graph:
        #     return [[]]
        # self.visited = set()
        # paths = list()
        # for i, vertex in enumerate(graph):
        #     if i not in self.visited:
        #         # vertex_list = list()
        #         # vertex_list.append(vertex)
        #         # visited.add(vertex)
        #         paths.append(self.explore(i, self.visited))
                
        # return paths
        return self.dfs(0, graph, [])
#%%
graph = [[1,2],[3],[3],[]]
ans = Solution()
print (ans.allPathsSourceTarget(graph))
                