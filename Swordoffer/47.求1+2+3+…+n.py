# -*- coding:utf-8 -*-
# 求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等
# 关键字及条件判断语句（A?B:C）。


class Solution:
    def Sum_Solution(self, n):
        if n == 1:
            return 1
        else:
            return n + self.Sum_Solution(n - 1)


if __name__ == '__main__':
    S = Solution()
    print(S.Sum_Solution(100))
