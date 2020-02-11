# -*- coding:utf-8 -*-
# 输入一颗二叉树的根节点和一个整数，
# 打印出二叉树中结点值的和为输入整数的所有路径。
# 路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
# (注意: 在返回值的list中，数组长度大的数组靠前)


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        result = []
        if not root:
            return result
        # 如果只有根节点或者找到叶子节点，我们就把其值返回
        if not root.left and not root.right and root.val == expectNumber:
            return [[root.val]]
        # 如果不是叶子节点，我们分别对根节点的左子树、右子树进行递归，注意修改变量:
        else:
            left = self.FindPath(root.left, expectNumber - root.val)
            right = self.FindPath(root.right, expectNumber - root.val)
            for item in left + right:
                result.append([root.val] + item)
            return result


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
