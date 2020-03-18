# -*- coding:utf-8 -*-
# 在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符，
# 并返回它的位置, 如果没有则返回 -1（需要区分大小写）


class Solution:
    def FirstNotRepeatingChar(self, s):
        dict = {}
        for ele in s:
            dict[ele] = 1 if ele not in dict else dict[ele] + 1
        for i in range(len(s)):
            if dict[s[i]] == 1:
                return i
        return -1

# 阿里达摩院机器翻译实习1面
class solution1:
    def __init__(self):
        self.dic = {}
        self.queue = []

    def FirstNotRepeatingChar(self, str):
        for i in str:
            if i not in self.dic:
                self.dic[i] = 1
                self.queue.append(i)
            else:
                self.dic[i] += 1
        for i in self.queue:
            if self.dic[i] == 1:
                return i


if __name__ == '__main__':
    S = Solution()
    print(S.FirstNotRepeatingChar("algkajgakgjkajlgjlo"))

    S1 = solution1()
    print(S1.FirstNotRepeatingChar("to"))