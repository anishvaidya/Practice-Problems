#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 10:02:49 2020

@author: vanish
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
import heapq
from typing import List

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        h = []
        for ll in lists:
            while ll:
                heapq.heappush(h, ll.val)
                ll = ll.next
        dummy = ListNode(None)
        ptr = dummy
        while h:
            ptr.next = ListNode(heapq.heappop(h))
            ptr = ptr.next
        return dummy.next
            
    
        # this is O(k) space
        h = []
        count = 0
        for ll in lists:
            if ll is not None:
                count += 1
                heapq.heappush(h, (ll.val, count, ll))
        dummy = ListNode(None)
        ptr = dummy
        while h:
            ptr.next = heapq.heappop(h)[2]
            ptr = ptr.next
            if ptr.next is not None:
                count += 1
                heapq.heappush(h, (ptr.next.val, count, ptr.next))
        return dummy.next