from collections import deque
class MyStack:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        self.queue1.append(x)
        while self.queue2:
            tmp = self.queue2.popleft()
            self.queue1.append(tmp)
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self) -> int:
        return self.queue2.popleft()

    def top(self) -> int:
        if self.queue2:
            return self.queue2[0]

    def empty(self) -> bool:
        return not bool(self.queue2)
