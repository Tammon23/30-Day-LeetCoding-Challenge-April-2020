class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minEl = None
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) == 0:
            self.minEl = x
            self.stack.append(x)
            return
        
        if x >= self.minEl:
            self.stack.append(x)
            return
        
        self.stack.append(2*x-self.minEl)
        self.minEl = x
        return
       
    def pop(self) -> None:
        if len(self.stack) == 0:
            return
        
        y = self.stack.pop()
        if y < self.minEl:
            self.minEl = 2 * self.minEl - y

    def top(self) -> int:
        stackLen = len(self.stack)
        if not stackLen:
            return None
        peek = self.stack[stackLen - 1]
        if peek < self.minEl:
            return self.minEl
        return peek

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return None
        return self.minEl


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
