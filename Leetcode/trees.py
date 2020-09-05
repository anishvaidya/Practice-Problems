#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 09:22:57 2019

@author: vanish
"""
#%%
class Tree():
    def __init__(self, value):
       self.data = value
       self.left = None
       self.right = None
# inorder left, root, right     
    def inorder(self, root):
       if root:
           self.inorder(root.left)
           print (root.data)
           self.inorder(root.right)
# preorder root, left, right
    def preorder(self, root):
        if root:
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)
            
# postorder left, right, root
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print (root.data)
            
    def isBSTUtil(self, root, mini, maxi):
        if root is None:
            return True
        if root.data > maxi or root.data < mini:
            return False
        return (self.isBSTUtil(root.left, mini, root.data - 1) and self.isBSTUtil(root.right, root.data + 1, maxi))
         
    def isBST(self, root):
        return self.isBSTUtil(root, float('-inf'), float('inf'))
        
 #%%
           
root = Tree(5)
root.left = Tree(2)
root.left.left = Tree(1)
root.left.right = Tree(3)
root.right = Tree(6)
print ("inorder")
root.inorder(root)
print ("preorder")
root.preorder(root)
print ("postorder")
root.postorder(root)
print ("Is BST")
root.isBST(root)

#%%

def divide(dividend, divisor):
    flag = 1
    if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
        flag = -1
        
    quotient = 0
    diff = abs(dividend) - abs(divisor)
    while (diff >= 0):
        quotient += 1
        dividend = diff
        diff = abs(dividend) - abs(divisor)
    return flag * quotient
    
print (divide(-290192019201,-1))

#%%
# Graph 
from collections import defaultdict

class Graph:
    def __init__(self):
        # self.n_vertices = n_vertices
        self.graph = defaultdict(list)
        
    def addEdge(self, node1, node2, weight):
        self.graph[node1].append([node2, weight])
        self.graph[node2].append([node1, weight])
        
    def solution(self, node, target, visited, path, min_list):
        stack = [node]
        while stack:
            for child in self.graph[node]:
                return
                
    def findPaths(self, node, target):
        visited = [False]
        
        
        
        
    