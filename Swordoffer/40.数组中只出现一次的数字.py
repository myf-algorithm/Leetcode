# -*- coding:utf-8 -*-
# 一个整型数组里除了两个数字之外，其他的数字都出现了两次。
# 请写程序找出这两个只出现一次的数字。。


# 1、异或思想，一个数与自己异或为0，一个数与0异或为自己
# 2、由于其它数字两两相同，所以所有数异或则得到这两个不同数的异或结果。取这个结果的第一个1作为标志位
# 3、这个标志的1，必须是：这两个数在该位一个为0，一个为1
# 4、这样可以将数组分为两组，一组在该标志位为1，一组在该标志位为0，这两个不同数字分别在这两组内
# 5、将两组内的数分别异或，得到两个结果则为这两个不同的数


class Solution:
    def FindNumsAppearOnce(self, array):
        ans, a1, a2, flag = 0, 0, 0, 1
        # ans是两个不重复元素异或的结果
        for num in array:
            ans = ans ^ num
        print(ans)
        while (ans):
            if ans % 2 == 0:
                ans = ans >> 1
                flag = flag << 1
            else:
                break
        # 根据异或结果1所在的最低位，把数字分为两半
        # 每一半都为：出现一次的数据和成对出现的数据
        for num in array:
            if num & flag:
                a1 = a1 ^ num
            else:
                a2 = a2 ^ num
        return a1, a2


if __name__ == "__main__":
    S = Solution()
    print(S.FindNumsAppearOnce([1, 2, 4, 4, 5, 5, 7, 7, 11, 2]))
