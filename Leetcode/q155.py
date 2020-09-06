'''
@author: vanish
'''

#%%
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = list()
        self.mins = list()

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.stack) == 1:
            self.mins.append(x) 
        else:
            if x <= self.mins[-1]:
                self.mins.append(x)

    def pop(self) -> None:
        val = self.stack.pop()
        if self.mins[-1] == val:
            self.mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()