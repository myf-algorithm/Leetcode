# -*- coding:utf-8 -*-
# 将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，
# 但是string不符合数字要求时返回0)，要求不能使用字符串转换整数的库函数。
# 数值为0或者字符串不是一个合法的数值则返回0。


class Solution:
    def StrToInt(self, s):
        flag = True
        pos = 1
        res = 0
        if s == '':
            return 0
        for i in s:
            if i == '+' or i == '-':
                if flag == True:
                    flag = False
                    if i == '+':
                        pos = 1
                    elif i == '-':
                        pos = -1
                    else:
                        return 0
                else:
                    return 0
            elif i >= '0' and i <= '9':
                flag = False
                res = res * 10 + int(i)
            else:
                return 0
        res = pos * res
        return res


S = Solution()
print(S.StrToInt('1234'))
