import collections
from tkinter import font


class MaxQueue:

    def __init__(self):
        self.stack = collections.deque()
        self.max = collections.deque()


    def max_value(self) -> int:
        return self.max[0]


    def push_back(self, value: int) -> None:
        self.stack.append(value)
        # 维护 max deque
        while self.max and value > self.max[-1]:
            self.max.pop()
        self.max.append(value)


    def pop_front(self) -> int:
        front = self.stack.popleft()
        if front == self.max[0]:
            self.max.popleft()
        return self.stack.popleft()



# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()