# -*- coding:utf-8 -*-
# 输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        def subtree(pRoot1, pRoot2):
            if pRoot1 == None and pRoot2 == None:
                return True
            if pRoot1 == None:
                return False
            if pRoot2 == None:
                return False
            if pRoot2.val == pRoot1.val:
                if pRoot2.left == None and pRoot2.right == None:
                    return True
                if subtree(pRoot1.left, pRoot2.left) and subtree(pRoot1.right, pRoot2.right):
                    return True
            return subtree(pRoot1.left, pRoot2) or subtree(pRoot1.right, pRoot2)

        if pRoot1 == None and pRoot2 == None:
            return False
        return subtree(pRoot1, pRoot2)


if __name__ == '__main__':
    S = Solution()
    root = TreeNode(0)
    node0 = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    node3 = TreeNode(4)
    node4 = TreeNode(5)
    node5 = TreeNode(6)

    root.left = node0
    root.right = node1
    node0.left = node2
    node0.right = node3
    node1.left = node4
    node1.right = node5

    # subtree
    node6 = TreeNode(1)
    node7 = TreeNode(3)
    node8 = TreeNode(4)
    node6.left = node7
    node6.right = node8

    print(S.HasSubtree(root, node6))
