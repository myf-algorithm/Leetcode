# -*- coding:utf-8 -*-
# 从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 等价于二叉树的广度优先遍历
    def Print(self, pRoot):
        if not pRoot:
            return []
        printArr = []
        stack = [pRoot]
        while stack:
            tmp = []
            tmp_stack = []
            for node in stack:
                tmp.append(node.val)
                if node.left:
                    tmp_stack.append(node.left)
                if node.right:
                    tmp_stack.append(node.right)
            printArr.append(tmp)
            stack = tmp_stack[:]
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
