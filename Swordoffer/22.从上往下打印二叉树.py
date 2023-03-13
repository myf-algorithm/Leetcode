# -*- coding:utf-8 -*-
# 从上往下打印出二叉树的每个节点，同层节点从左至右打印。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def PrintFromTopToBottom(self, root):
        if root is None:
            return []
        queue = [root]
        res = []
        while queue:
            cur_node = queue.pop(0)
            res.append(cur_node.val)
            if cur_node.left is not None:
                queue.append(cur_node.left)
            if cur_node.right is not None:
                queue.append(cur_node.right)
        return res


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
    print(S.PrintFromTopToBottom(root))
