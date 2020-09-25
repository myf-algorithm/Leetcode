# encoding:utf-8
# 9.25 搜狗笔试2
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 返回一行字符串，表示原文。
# @param s1 string字符串一维数组 N*N的01矩阵，表示解密纸，0表示透明，1表示涂黑
# @param s2 string字符串一维数组 字符矩阵，表示密文
# @return string字符串
#


class Solution:
    def rotateMatrix(self, mat, n):
        res = []
        for i in range(0, n):
            row = []
            for j in range(0, n):
                row.append(mat[n - j - 1][i])
            res.append(row)
        return res

    def rotatePassword(self, s1, s2):
        n = len(s1)
        mat_in = []
        for i in s1:
            mat_in.append(list(i))
        res = ""
        for i in range(n):
            for j in range(n):
                if mat_in[i][j] == '0':
                    res += s2[i][j]
        for _ in range(3):
            mat_in = self.rotateMatrix(mat_in, n)
            for i in range(n):
                for j in range(n):
                    if mat_in[i][j] == '0':
                        res += s2[i][j]
        return res


S = Solution()
print(S.rotatePassword(["1101", "1010", "1111", "1110"], ["ABCD", "EFGH", "IJKL", "MNPQ"]))
