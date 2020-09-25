# _*_ encoding:utf-8 _*_
# 9.25 搜狗笔试1

class Interval:
    def __init__(self, a=0, b=0):
        self.start = a
        self.end = b


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 返回Interval类，start代表汪仔最少做对了多少道题，end代表汪仔最多做对了多少道题。
# @param n int整型 选择题总数
# @param k int整型 朋友做对的题数
# @param str1 string字符串 长度为n只包含ABCD的字符串，其中第i个代表汪仔第i题做出的选择
# @param str2 string字符串 长度为n只包含ABCD的字符串，其中第i个代表朋友第i题做出的选择
# @return Interval类
#
class Solution:
    def solve(self, n, k, str1, str2):
        same_cnt = 0
        dif_cnt = 0
        for i in range(len(str1)):
            if str1[i] == str2[i]:
                same_cnt += 1
            else:
                dif_cnt += 1

        if same_cnt >= k:
            max_cnt = k + dif_cnt
        else:
            max_cnt = n - (k - same_cnt)

        if k > dif_cnt:
            min_cnt = k - dif_cnt
        else:
            min_cnt = 0

        res = Interval(min_cnt, max_cnt)
        return res
