#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 15:30:25 2020

@author: vanish
"""

from typing import List
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        database = {}
        answer = []
        for path in paths:
            splits = path.split(" ", 1)
            location = splits[0]
            for file in splits[1].split(" "):
                data = file.split("(")
                name = data[0]
                content = data[1][:-1]
                if content in database:
                    database[content].append(location+"/"+name)
                else:
                    database[content] = [location+"/"+name]
        for values in database.values():
            if len(values) > 1:
                answer.append(values)
        return answer
    
#%%

paths = ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
ans = Solution()
print (ans.findDuplicate(paths))