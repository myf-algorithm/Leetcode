# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []  # 普通的栈
        self.minstack = []  # 保存最小值的栈
        self.minm = float('inf')  # 记录当前的最小值

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


# 两个栈的实现方法
class Solution1:
    def __init__(self):
        self.stackData = []
        self.stackMin = []

    def push(self, num):
        if not self.stackMin:
            self.stackMin.append(num)
        elif num <= self.getMin():
            self.stackMin.append(num)
        else:
            self.stackMin.append(self.stackMin[-1])
        self.stackData.append(num)

    def pop(self):
        if not self.stackData:
            return "Your stack is empty."
        self.stackMin.pop()
        return self.stackData.pop()

    def getMin(self):
        if not self.stackMin:
            return "Your stack is empty."
        return self.stackMin[-1]

    def getMinStack(self, op):
        # write code here
        res = []
        if op == []:
            return res
        for i in op:
            if i[0] == 1:
                self.push(i[1])
            elif i[0] == 2:
                self.pop()
            elif i[0] == 3:
                res.append(self.getMin())
        return res


if __name__ == '__main__':
    S = Solution()
    S.push(2)
    S.push(1)
    S.push(3)
    S.push(4)
    S.push(5)
    print(S.top())
    print(S.min())
