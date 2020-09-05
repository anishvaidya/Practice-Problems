#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 16:20:21 2019

@author: vanish
"""
#%%
# Longest substring
longest_substring_len = 1
def longest(s):
#    s = 'dvdf'
#    longest_substring_len = 0
    global longest_substring_len 
    current_substring_len = 1
    if len(s) != 0:
#        longest_substring_len = 1
        longest_substring = [s[0]]
        for i in range (1, len(s)):
            if (s[i] not in longest_substring):
                longest_substring.append(s[i])
                print(longest_substring)
                current_substring_len += 1
                if (current_substring_len > longest_substring_len):
                    longest_substring_len = current_substring_len 
                
            
            elif (s[i] in longest_substring):
#                current_substring_len = 1
#                if (current_substring_len > longest_substring_len):
                indx = longest_substring.index(s[i])
                s = s[indx + 1:]
                print("new s", s)
                return longest(s)
                pass
        # print (s[i], "\n")
    else:
#        longest_substring = []
        longest_substring_len = 0
        pass
#    print (longest_substring)
    return longest_substring_len
longest('dvdf')
#%%
# Longest substring
def lengthOfLongestSubstring(s: str) -> int:
        longest = 0
        list_of_chars = list(s)
        sub_list_of_chars = []
        for char in list_of_chars:
            print(sub_list_of_chars, "->", char)
            if char in sub_list_of_chars:
                length_of_sub_list = len(sub_list_of_chars)
                if length_of_sub_list > longest:
                    longest = length_of_sub_list
                sub_list_of_chars = sub_list_of_chars[sub_list_of_chars.index(char)+1:]
            sub_list_of_chars.append(char)
        length_of_sub_list = len(sub_list_of_chars)
        if length_of_sub_list > longest:
            longest = length_of_sub_list
        return longest
lengthOfLongestSubstring('dvdf')
#%%

def lengthOfLongestSubstring(s: str) -> int:
    longest_substring_len = 0
    longest_substring = []
    list_s = list(s)

    for i in list_s:
        # print ("for", i)
        if (i in longest_substring):
            current_substring_len = len(longest_substring)
            if (current_substring_len > longest_substring_len):
                longest_substring_len = current_substring_len 
            longest_substring = longest_substring[longest_substring.index(i) + 1:]
        longest_substring.append(i)
                
        # print (s[i], "\n")
    current_substring_len = len(longest_substring)
    if (current_substring_len > longest_substring_len):
        longest_substring_len = current_substring_len 
    print (longest_substring)
    return longest_substring_len
lengthOfLongestSubstring('')