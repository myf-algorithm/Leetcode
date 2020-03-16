# -*- coding:utf-8 -*-
#
# 请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，
# 第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Print(self, pRoot):
        if not pRoot:
            return []
        printArr = []
        flag = 0
        stack = [pRoot]
        while stack:
            tmp = []  # 定义临时列表，存储节点数值
            tmp_stack = []  # 定义临时列表，作为堆栈，存储二叉树每层的节点
            for node in stack:
                tmp.append(node.val)
                if node.left:
                    tmp_stack.append(node.left)  # 保存节点的左子节点
                if node.right:
                    tmp_stack.append(node.right)  # 保存节点的右子节点
            if flag % 2 == 1:
                printArr.append(tmp[::-1])  # 存储printArr结果，反转tmp值列表
            else:
                printArr.append(tmp)  # 存储printArr结果，tmp值列表
            flag = flag + 1
            stack = tmp_stack[:]  # 更新stack
        return printArr


if __name__ == '__main__':
    S = Solution()
    root = TreeNode(0)
    node0 = TreeNode(2)
    node1 = TreeNode(3)
    node2 = TreeNode(4)
    node3 = TreeNode(2)
    node4 = TreeNode(4)
    node5 = TreeNode(2)
    root.left = node0
    root.right = node1
    node1.left = node2
    node1.right = node3
    node3.left = node4
    node4.left = node5
    print(S.Print(root))
