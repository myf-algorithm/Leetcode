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

if __name__ == '__main__':
    S = Solution()
    print(S.FirstNotRepeatingChar("algkajgakgjkajlgjlo"))