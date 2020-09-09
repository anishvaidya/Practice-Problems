#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 11:12:56 2020

@author: vanish
"""

#%%
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        seen = 0
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        if (count == 0 or count == k or k == 0 or count == 1):
            return head
        if k > count:
            go_ahead = count - (k % count)
        else:
            go_ahead = count - k
        if go_ahead == count:
            return head
        curr = head
        seen = 0
        while seen < go_ahead:
            seen += 1
            prev = curr
            curr = curr.next
        new_head = curr
        before_old_head = new_head
        prev.next = None
        while before_old_head.next:
            before_old_head = before_old_head.next
        before_old_head.next = head
        return new_head
        
#%%



