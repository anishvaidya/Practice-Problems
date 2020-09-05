#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 11:23:23 2019

@author: vanish
"""
#%%
def myAtoi(str: str) -> int:
    if (len(str) == 0):
            return 0
    str = str.lstrip()
    answer = []
    sign = ["-", "+"]
    if (str[0] in sign or str[0].isdigit()):
        for char in str:
            print ("current char", char)
            if (char == "+" or char == "-"):
                answer.append("")
                or char == "." or char.isdigit()):
                answer.append(char)
                print(char, "appended")
            elif (char == " "):
                res = int(float("".join(answer)))
                return max(-2**31, min(res,2**31-1))
        print (answer)
        res = int(float("".join(answer)) )
        return max(-2**31, min(res,2**31-1))
    else:
        return 0
#    return res
myAtoi("  -123.2 as 1")    
#%%
def atoi(str: str) -> int:
    str = str.lstrip()
    spaces_ended = False
    digits = '0123456789'
    signs = '+-'
    sign = 0
    answer = []
    if (len(str) == 0): return 0
    for char in str:
        if char in signs and not sign:
            sign = -1 if char == '-' else 1
        elif char in digits:
            sign = 1 if not sign else sign
            answer.append(char)
        else: 
            break
    number = 0
    print (answer)
    for i in range(0, len(answer)):
        number += digits.index(answer[i]) * 10 ** (len(answer) - i - 1)
    number *= sign
    
    
    return max(-2 ** 31, min(number, 2 ** 31 -1))

    
atoi('-213 321')

#%%