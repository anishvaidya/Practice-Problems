#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 08:23:59 2019

@author: vanish
"""
#%%
from typing import List
def longestCommonPrefix(strs: List[str]) -> str:
    if not strs: return ""
    prefix = min(strs, key = len)
    for i, char in enumerate(prefix):
        for strchar in strs:
            if strchar[i] != char:
                prefix = prefix[:i]
#    print(strs)
    

    return prefix
s = ["flower","flow","flight"]  
longestCommonPrefix(s)    
#%%    
def buddyStrings(A: str, B: str) -> bool:
#    if len(A) != len(B):
#        return False
#    C = list(A)
#    B = list(B)
#    for i in range(len(C)):
#        for j in range(i + 1, len(C)):
#           temp = C[i]
#           C[i] = C[j]
#           C[j] = temp
#           if C == B:
#               return True
#           else: C = list(A)
#    return False
    lenA = len(A)
    lenB = len(B)
    if lenA != lenB: return False
    mismatch1 = -1
    mismatch2 = -1
    count = 0
    if (A == B):
        return (len(A) - len(set(A)) >= 1)
    for i in range(lenA):
        if A[i] != B[i]: 
            count+= 1
            if count > 2: return False
            mismatch1 = mismatch2
            mismatch2 = i
    return (count == 2 and A[mismatch1] == B[mismatch2] and A[mismatch2] == B[mismatch1])
A = "aa"
B = "aa"
buddyStrings(A,B)
#%%
import math
def intToRoman(num: int) -> str:
        map = {'1': 'I', '5': 'V', '10': 'X', '50': 'L', '100': 'C', '500': 'D', '1000': 'M', '4': 'IV', '9': 'IX', '40': 'XL', '90' : 'XC', '400': 'CD', '900': 'CM'}
        value = []
        roman = []
        #print(map['1'])
        max_base = math.floor(math.log(num, 10))
        while max_base >= 0 and num > 0:
            max_base = math.floor(math.log(num, 10))
            print (max_base)
            count = num // 10 ** max_base
            print(count)
            value.append([count, max_base])
            num -= count * 10 ** max_base
            
        print(value)
        for i in range(len(value)):
            print("count, maxbase", value[i][0], value[i][1])
            roman.append(map[i] if (map[i] == count * 10 ** maxbase))
#        z = 10 ** max_base
        #value1 = map[str(z)]
        #value1 = map[str(1000)]
#        print (z)
#        div_1000 = num // 1000
#        div_100 = num // 100
        
intToRoman(2542)
#%%
def intToRoman(num: int) -> str:
        roman = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        result = ""
        for letter, n in zip(roman, nums):
            print(letter, n)
            result += letter * int(num / n)
            num %= n
        return result
intToRoman(2542)
#%%
from typing import List
def threeSum(nums: List[int]) -> List[List[int]]:
    three_sum = []
    nums.sort()
    length = len(nums)
    for i in range(length - 2):
        if nums[i] > 0: break
        if i > 0 and nums[i] == nums[i - 1]: continue
        l, r = i + 1, length - 1
        while l < r:
            total = nums[i] + nums[l] + nums[r]
            if total < 0:
                l += 1
            elif total > 0:
                r -= 1
            else:
                print (total)
                three_sum.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                l += 1
                r -= 1
    return three_sum
            
threeSum([-1, -1, -1, 0, 1 ,2])    
#%%
from typing import List
def threeSumClosest(nums: List[int], target: int) -> int:
    closest = 9999
    nums.sort()
    print(nums)
    length = len(nums)
    old_sum = 9999
    for i in range(length - 2):
        l, r = i + 1, length - 1
        while l < r:
            total = nums[i] + nums[l] + nums[r]
            print("old sum", old_sum)
            old_sum = total
            print ("total is",total)
            print("l:", l, "r:",r)
            if abs(target - total) < abs(target - closest): closest = total
            if total < target:
                print(total, "<", target)
                l += 1
            elif total > target:
                r -= 1
            else: break
    return closest
            
threeSumClosest([1,2,4,8,16,32,64,128], 82) 
#%%
def longestPalindrome(self, s: str) -> str:
    if s[0] != s[-1]:
    
    
    
    return longest

longestPalindrome("babad")

#%%
def letterCombinations(digits: str) -> List[str]:
    mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    letter_list = [''] if digits else []
    for num in digits:
#        letter = ''
#        for val in range(len(mapping[num])):
#            letter += mapping[num][val]
#        letter_list.append(letter)
#        for p in letter_list:
#            for q in mapping[num]:
#                letter_list = [p + q]
        letter_list = [p + q for p in letter_list for q in mapping[num]]
                
    return letter_list

letterCombinations('23')
#%%

def validBrackets(s: str) -> bool:
    stack = []
        balanced = True
        mapping = {')': '(', ']': '[', '}': '{'}
        for i in range(len(s)):

            if (s[i] == '(' or s[i] == '[' or s[i] == '{'):
                stack.append(s[i])
                # print (stack)
            elif (s[i] == ')' or ']' or '}'):
                if (len(stack) == 0):
                    return False
                popped_char = stack.pop()
                if (mapping[s[i]] == popped_char):
                    balanced = True
                else:
                    return False
        if (len(stack) > 0):
            balanced = False
        return balanced

validBrackets('[()][]')

#%%
#def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        start = solution = ListNode(None)
        while l1 and l2:
            if (l1.val < l2.val):
                                
                solution.next = ListNode(l1.val)
                # solution.next = None
                l1 = l1.next

            else:
                solution.next = ListNode(l2.val)
                # solution.next = None
                l2 = l2.next
            solution = solution.next
        # solution = l1 or l2
        while l1:
            solution.next = ListNode(l1.val)
                # solution.next = None
            l1 = l1.next
            solution = solution.next
        while l2:
            print ("element", l2.val)
            solution.next = ListNode(l2.val)
                # solution.next = None
            l2 = l2.next
            solution = solution.next
        return start.next
    
    #%%
from typing import List    
def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    print (nums)
    i = 0
    operations = 0
    while i < len(nums):
        if operations == len(nums):
            break
        else:
            if nums[i] == 0:
                print ("popped", nums[i])
                
                nums.pop(i)
                nums.append(0)
                i -= 1
            operations += 1
            i += 1
    print (nums)
    
moveZeroes([1,2,0,3,5])
#%%
#Implement strStr()
def strStr(haystack: str, needle: str) -> int:
    for i in range(len(haystack) - len(needle) + 1):
        if (needle == haystack[i: i + len(needle)]):
            return i
    return -1

strStr("abcde", "cd")

#%%
def repeatedSubstringPattern(s: str) -> bool:
    for i in range(0, len(s) - 1):
        n = len(s) // (i + 1)
        if len(s) % (i + 1) == 0:
           if (n * s[0: i + 1] == s):
               print ("sub is" , n * s[0: i + 1], "is =", s)
               return True
           else:
               print ("sub is" , n * s[0: i + 1])
               continue
        else:
            continue
    return False
    
        
repeatedSubstringPattern("abdabdab")
#%%
import math
def repeatedStringMatch(A: str, B: str) -> int:
    lenA, lenB = len(A), len(B)
#        if A[0] == B[0]:
#            n = math.ceil(lenB / lenA) 
#        else:
#            n = math.ceil(lenB / lenA)  + 1
    n = math.ceil(lenB / lenA)
    print (n)
#        for i in range((n * lenA) - lenB + 1):
#            if (B == newA[i: i + len(B)]):
#                return n
    for i in range(2):
        if B in (A * (n + i)):
            return (n + i)
        
    return -1

    
    
    
    
repeatedStringMatch("aa", "a")
#%%
def countBinarySubstrings(s: str) -> int:
    groups = [1]
    for i in range(1, len(s)):
        if s[i-1] != s[i]:
            groups.append(1)
        else:
            groups[-1] += 1
    print (groups)
    ans = 0
    
countBinarySubstrings("0001110011")
