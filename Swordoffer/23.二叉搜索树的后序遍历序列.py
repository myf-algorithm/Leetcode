# -*- coding:utf-8 -*-
# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
# 如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。


class Solution:
    def VerifySquenceOfBST(self, sequence):
        if len(sequence) == 0:  # 如果序列长度为0，返回False
            return False
        if len(sequence) == 1 or len(sequence) == 2:
            return True  # 如果序列长度为1或2，返回True
        else:
            root = sequence.pop(-1)  # 弹出序列的最后一个节点为根节点
            sign = 0
            for i in range(len(sequence)):
                if sequence[i] > root:  # 已经找到比根节点大的元素
                    sign = 1  # 将标志向量置1
                if (sign == 1) and (sequence[i] < root):    # 再次找到比根节点小的元素
                    return False
            # 递归验证左子树和右子树的后序遍历序列
            return self.VerifySquenceOfBST(sequence[:i]) and self.VerifySquenceOfBST(sequence[i:])


if __name__ == '__main__':
    S = Solution()
    print(S.VerifySquenceOfBST([1, 2, 3, 4, 5, 6]))
