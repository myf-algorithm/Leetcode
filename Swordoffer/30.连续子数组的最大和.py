# -*- coding:utf-8 -*-
# HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。
# 今天测试组开完会后,他又发话了:在古老的一维模式识别中,常常需要计算连续子向量的最大和,
# 当向量全为正数的时候,问题很好解决。但是,如果向量中包含负数,是否应该包含某个负数,
# 并期望旁边的正数会弥补它呢？例如:{6,-3,-2,7,-15,1,2,2},
# 连续子向量的最大和为8(从第0个开始,到第3个为止)。给一个数组，
# 返回它的最大连续子序列的和，你会不会被他忽悠住？(子向量的长度至少是1)


class Solution:
    def FindGreatestSumOfSubArray(self, array):
        max_sum = array[0]
        pre_sum = 0  # pre_sum记录先前数组元素之和
        for i in array:
            if pre_sum < 0:  # 如果小于0，则将pre_sum设置为当前元素
                pre_sum = i
            else:
                pre_sum += i  # 如果大于0，继续累加当前元素
            if pre_sum > max_sum:  # 判断是否跟新max_sum
                max_sum = pre_sum
        return max_sum


if __name__ == '__main__':
    S = Solution()
    print(S.FindGreatestSumOfSubArray([1, 2, 3, -100, 5, 6, 7, 0]))
