# -*- coding:utf-8 -*-
# 给定一棵二叉搜索树，请找出其中的第k小的结点。
# 例如，（5，3，7，2，4，6，8）中，按结点数值大小顺序第三小结点的值为4。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def KthNode(self, pRoot, k):
        stack = []
        while True:
            if pRoot:  # 一直遍历到pRoot的最左子节点
                stack.append(pRoot)
                pRoot = pRoot.left
            else:
                if not stack:
                    return
                pRoot = stack.pop()
                k = k - 1
                if k == 0:
                    return pRoot.val
                else:
                    pRoot = pRoot.right


# 递归中序遍历写法
class Solution1:
    def KthNode(self, pRoot, k):
        numRes = []

        def inOreder(pRoot):
            if pRoot == None:
                return None
            inOreder(pRoot.left)
            numRes.append(pRoot)
            inOreder(pRoot.right)

        inOreder(pRoot)
        if len(numRes) < k or k < 1:
            return None
        return numRes[k - 1]


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
    print(S.KthNode(root, 1))
