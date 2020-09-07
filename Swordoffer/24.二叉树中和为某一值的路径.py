# -*- coding:utf-8 -*-
# 输入一颗二叉树的根节点和一个整数，
# 打印出二叉树中结点值的和为输入整数的所有路径。
# 路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
# (注意: 在返回值的list中，数组长度大的数组靠前)

from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res, path = [], []

        def dfs(root, sum):
            if not root:
                return
            path.append(root.val)
            sum -= root.val
            if sum == 0 and not root.left and not root.right:
                res.append(list(path))
            dfs(root.left, sum)
            dfs(root.right, sum)
            path.pop()

        dfs(root, sum)
        return res


class Solution1:
    def pathSum(self, root, sum):
        # write code here
        res = []
        path = []
        self.dfs(root, res, sum, path)
        return res

    def dfs(self, root, res, sum, path):
        if root is None:
            return
        if not root.left and not root.right and sum == root.val:
            res.append(path + [root.val])
            return
        path.append(root.val)
        self.dfs(root.left, res, sum - root.val, path)
        self.dfs(root.right, res, sum - root.val, path)
        path.pop()


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
    print(S.FindPath(root, 4))
