#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 11:59:06 2020

@author: vanish
"""
'''
    def compress(self, chars: List[str]) -> int:
        length = 0
        if len(chars) == 0 or len(chars) == 1:
            return len(chars)
        i = 0
        count = 1
        while(i < len(chars)):
            try:
                next_char = chars[i + 1]
            except (ValueError, IndexError):
                next_char = chr(33)
            if chars[i] == next_char:
                count += 1
                i += 1
            else:
                if count == 1:
                    length += 1
                elif count > 1:
                    length += 1 + len(str(count))
                count = 1
                i += 1
        return length
'''


from typing import List
#%%
class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 0 or len(chars) == 1:
            return len(chars)
        i = 0
        count = 1
        while(i < len(chars)):
            if i < len(chars) - 1:
                next_char = chars[i + 1]
            else:
                next_char = chr(33)
            if chars[i] == next_char:
                del chars[i + 1]
                count += 1
                # i += 1
            else:
                if count > 1:
                    count = list(str(count))
                    for number in count:
                        chars.insert(i + 1, number)
                        i += 1
                count = 1
                i += 1
        print (chars)
        return len(chars)   
    
#%%

#%%
chars = ["a","b","b","c","c","c"]
ans = Solution()
print (ans.compress(chars))

                
        