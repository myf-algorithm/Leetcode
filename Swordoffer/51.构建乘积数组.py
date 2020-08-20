# -*- coding:utf-8 -*-
# 给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],
# 其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。
# 不能使用除法。


class Solution:
    def multiply(self, A):
        size = len(A)
        # 初始化
        B = [1] * size

        # 计算前边的部分
        # 下三角: B[i]=A[0]A[1]A[2]..A[i−1] = B[i−1]A[i−1]
        for i in range(1, size):
            B[i] = B[i - 1] * A[i - 1]

        # 计算后面的部分
        # 上三角（从最后往前）tmp=A[−1]A[−2]A[−3]...
        tmp = 1
        for i in range(size - 2, -1, -1):
            tmp = tmp * A[i + 1]
            B[i] = B[i] * tmp
        return B



if __name__ == '__main__':
    S = Solution()
    print(S.multiply([2, 1, 3, 1, 4]))
