# -*- coding: utf-8 -*-

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s = dict()
        for c in s:
            count_s[c] = count_s.get(c, 0) + 1
        for c in t:
            if c in count_s.keys():
                count_s[c] -= 1
            else:
                return False
        for val in count_s.values():
            if val != 0:
                return False
        return True