# -*- coding:utf-8 -*-
# 输入一棵二叉树，判断该二叉树是否是平衡二叉树。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Treeheight(self, pRoot):
        if pRoot == None:
            return 0
        if pRoot.left == None and pRoot.right == None:
            return 1
        lh = self.Treeheight(pRoot.left)
        rh = self.Treeheight(pRoot.right)
        return max(lh, rh) + 1

    def IsBalanced_Solution(self, pRoot):
        if pRoot == None:
            return True
        return abs(self.Treeheight(pRoot.left) - self.Treeheight(pRoot.right)) <= 1


if __name__ == "__main__":
    S = Solution()
    root = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    node3 = TreeNode(1)
    node4 = TreeNode(2)
    root.left = node1
    root.right = node2
    node1.left = node3
    node2.left = node4
    print(S.IsBalanced_Solution(root))
