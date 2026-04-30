class MinStack:
    # maintain a min and a stack. push/pop follows LIFO. top is the last added element.
    # pop, top and getMin will always be called on non-empty stacks.
    # key: use another stack to keep track of global min,
    # when appending a value greater than mininum, we append the minimum again
    # otherwise we append that value to the top. this way the top is always the minimum.
    def __init__(self):
        self.minstack = []
        self.stack = []
        self.n = 0

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minstack:
            self.minstack.append(val)
        elif val <= self.minstack[self.n - 1]:
            self.minstack.append(val)
        else:
            self.minstack.append(self.minstack[self.n - 1])
        self.n += 1

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        self.n -= 1

    def top(self) -> int:
        return self.stack[self.n - 1]

    def getMin(self) -> int:
        return self.minstack[self.n - 1]
