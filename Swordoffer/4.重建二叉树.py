# -*- coding:utf-8 -*-
# 输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
# 假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
# 例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，
# 则重建二叉树并返回。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def reConstructBinaryTree(self, pre, tin):
        if pre == []:
            return
        val = pre[0]
        idx = tin.index(val)
        ltin = tin[0:idx]
        rtin = tin[(idx + 1):]
        lpre = pre[1:(1 + len(ltin))]
        rpre = pre[(1 + len(ltin)):]
        root = TreeNode(val)
        root.left = self.reConstructBinaryTree(lpre, ltin)
        root.right = self.reConstructBinaryTree(rpre, rtin)
        return root

    def preorder(self, pRoot):
        if pRoot is None:
            return
        print(pRoot.val, end=" ")
        self.preorder(pRoot.left)
        self.preorder(pRoot.right)

    def inorder(self, pRoot):
        if pRoot is None:
            return
        self.inorder(pRoot.left)
        print(pRoot.val, end=" ")
        self.inorder(pRoot.right)

if __name__ == '__main__':
    S = Solution()
    pre = [1, 2, 4, 7, 3, 5, 6, 8]
    tin = [4, 7, 2, 1, 5, 3, 8, 6]
    root = S.reConstructBinaryTree(pre, tin)
    S.preorder(root)
    print()
    S.inorder(root)
