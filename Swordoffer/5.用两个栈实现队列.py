# -*- coding:utf-8 -*-
# 用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。

class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        # 将新元素压入堆栈stack1
        self.stack1.append(node)

    def pop(self):
        # stack2非空，输出stack2的栈顶元素
        if len(self.stack2):
            return self.stack2.pop()
        # stack2是空的，把stack1中的栈顶元素依次压入stack2中
        # 如此处理之后
        # stack1中的栈顶元素被压入stack2的栈底
        # stack1中的栈底元素被压入stack2的栈顶
        # stack2下次进行pop时，输出stack1中的栈底元素
        # 如此实现了stack1中的元素，按照先入先出的顺序输出
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        # 判断stack2是否是空的，非空则输出，空则return
        if self.stack2:
            return self.stack2.pop()
        else:
            return


if __name__ == '__main__':
    S = Solution()
    S.push(1)
    print(S.pop())
    print(S.pop())
