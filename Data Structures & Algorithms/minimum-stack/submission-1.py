class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if (val <= self.min):
            self.min = val
            self.min_stack.append(val)
        

    def pop(self) -> None:
        ele = self.stack.pop()
        if ele == self.min_stack[-1]:
            self.min_stack.pop()
            if self.min_stack:
                self.min = self.min_stack[-1]
            else:
                self.min = float('inf')
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return int(self.min)

        
