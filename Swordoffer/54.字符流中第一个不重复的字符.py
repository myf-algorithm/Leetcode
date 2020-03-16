# -*- coding:utf-8 -*-
# 请实现一个函数用来找出字符流中第一个只出现一次的字符。
# 例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。
# 当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。


class Solution:
    def __init__(self):
        self.queue = []
        self.memory = dict()

    # 返回对应char
    def FirstAppearingOnce(self):
        while len(self.queue) and self.memory[self.queue[0]] > 1:
            self.queue.pop(0)
        return self.queue[0] if len(self.queue) else '#'

    def Insert(self, char):
        if char not in self.memory:
            self.memory[char] = 0
        self.memory[char] += 1
        if self.memory[char] == 1:
            self.queue.append(char)


if __name__ == '__main__':
    S = Solution()
    S.Insert('1')
    S.Insert('2')
    S.Insert('1')
    S.Insert('1')
    print(S.FirstAppearingOnce())
