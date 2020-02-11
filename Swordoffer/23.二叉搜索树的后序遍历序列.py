# -*- coding:utf-8 -*-
# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
# 如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。


class Solution:
    def VerifySquenceOfBST(self, sequence):
        if len(sequence) == 0:
            return False
        if len(sequence) == 1 or len(sequence) == 2:
            return True
        else:
            root = sequence.pop(-1)
            sign = 0
            for i in range(len(sequence)):
                if sequence[i] > root:
                    sign = 1
                if (sign == 1) and (sequence[i] < root):
                    return False
            return self.VerifySquenceOfBST(sequence[:i]) and self.VerifySquenceOfBST(sequence[i:])


if __name__ == '__main__':
    S = Solution()
    print(S.VerifySquenceOfBST([1, 2, 3, 4, 5, 6]))
