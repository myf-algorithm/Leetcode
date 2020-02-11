# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.minstack = []
        self.minm = float('inf')

    def push(self, node):
        self.stack.append(node)
        if node < self.minm:
            self.minm = node
            self.minstack.append(self.minm)

    def pop(self):
        if self.stack != []:
            if self.stack[-1] == self.minm:
                self.minstack.pop()
            self.stack.pop()

    def top(self):
        if self.stack != []:
            return self.stack[-1]
        else:
            return None

    def min(self):
        return self.minstack[-1]

if __name__ == '__main__':
    S = Solution()
    S.push(2)
    S.push(1)
    S.push(3)
    S.push(4)
    S.push(5)
    print(S.top())
    print(S.min())
