class MinStack:

    def __init__(self):
        self.whole_stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        self.whole_stack.append(x)
        if not self.min_stack or self.min_stack[-1] >= x:
            self.min_stack.append(x)

    def pop(self)-> None:
        if self.whole_stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.whole_stack[-1]


    def min(self) -> int:
        return self.min_stack[-1]


    # def __init__(self):
    #     """
    #     initialize your data structure here.
    #     """
    #     self.stack = []

    # def push(self, x: int) -> None:
    #     self.stack.append(x)


    # def pop(self) -> None:
    #     self.stack.pop()

    # def top(self) -> int:
    #     if not self.stack:
    #         return 0
    #     else:
    #         return self.stack[-1]


    # def min(self) -> int:
    #     return min(self.stack)



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()