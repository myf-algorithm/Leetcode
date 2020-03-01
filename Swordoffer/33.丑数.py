# -*- coding:utf-8 -*-
# 把只包含质因子2、3和5的数称作丑数（Ugly Number）。
# 例如6、8都是丑数，但14不是，因为它包含质因子7。
# 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。


class Solution:
    def GetUglyNumber_Solution(self, index):
        if index == 0:
            return 0
        baselist = [1]  # 1作为特殊数字直接保存
        min2 = min3 = min5 = 0
        curnum = 1
        while curnum < index:
            # 得到T2 * 2，T3 * 3，T5 * 5中最小的那个数
            minnum = min(baselist[min2] * 2, baselist[min3] * 3, baselist[min5] * 5)
            baselist.append(minnum)
            # 找到第一个乘以2的结果大于当前最大丑数M的数字，也就是T2
            while baselist[min2] * 2 <= minnum:
                min2 += 1
            # 找到第一个乘以3的结果大于当前最大丑数M的数字，也就是T3
            while baselist[min3] * 3 <= minnum:
                min3 += 1
            # 找到第一个乘以5的结果大于当前最大丑数M的数字，也就是T5
            while baselist[min5] * 5 <= minnum:
                min5 += 1
            curnum += 1
        return baselist[-1]


if __name__ == '__main__':
    S = Solution()
    print(S.GetUglyNumber_Solution(25))
