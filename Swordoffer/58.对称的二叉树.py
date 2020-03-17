# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetrical(self, pRoot):
        if not pRoot:
            return True
        return self.recursiveTree(pRoot.left, pRoot.right)

    def recursiveTree(self, left, right):
        if not left and not right:  # 左右子节点都为空
            return True
        if not left or not right:  # 左右子节点其中一个为空
            return False
        if left.val == right.val:  # 左右子节点都存在，并且值相等，进行下一次递归
            return self.recursiveTree(left.left, right.right) and self.recursiveTree(left.right, right.left)
        return False


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
    print(S.isSymmetrical(root))
