#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 12:40:00 2020

@author: vanish
"""
from collections import deque
class BrowserHistory:

    def __init__(self, homepage: str):
        self.pages = [homepage]
        self.pointer = 0

    def visit(self, url: str) -> None:
        while (len(self.pages) - 1 > self.pointer):
            self.pages.pop()
        self.pages.append(url)
        self.pointer += 1

    def back(self, steps: int) -> str:
        self.pointer = max(0, self.pointer - steps)
        return self.pages[self.pointer]

    def forward(self, steps: int) -> str:
        self.pointer = min(self.pointer + steps, len(self.pages) - 1)
        return self.pages[self.pointer]

#%%
# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

browserHistory = BrowserHistory("leetcode.com")
browserHistory.visit("google.com")
browserHistory.visit("facebook.com")
browserHistory.visit("youtube.com")
browserHistory.back(1)
browserHistory.back(1)
browserHistory.forward(1)
browserHistory.visit("linkedin.com")
browserHistory.forward(2)
browserHistory.back(2)
browserHistory.back(7)