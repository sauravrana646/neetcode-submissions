class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.min_num = 2**32

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_num >= val:
            self.min_num = val
            self.min_stack.append(val)

    def pop(self) -> None:
        poped = self.stack.pop()
        if poped == self.min_num:
            self.min_stack.pop()
            if self.min_stack != []:
                self.min_num = self.min_stack[-1]
            else:
                self.min_num = 2**32

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
