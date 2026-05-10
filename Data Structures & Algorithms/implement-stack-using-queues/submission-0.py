class MyStack:

    def __init__(self):
        self.q1 = deque() # the main queue storing added elements in reverse order to simulate LIFO
        self.q2 = deque()

    def push(self, x: int) -> None:
        # push x to q2 and then move all elements from q1 to q2, now x is at the top of q2
        # and then swap q1 and q2. 
        # after this, we have the newly pushed element at the top of q1
        # next time we push another x, we push into q2 first,
        # and then move q1 content to q2, the previously added element comes after the newly pushed element
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1 # now we have q1 storing all elements and q2 empty

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return len(self.q1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()