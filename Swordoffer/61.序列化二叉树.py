# -*- coding:utf-8 -*-
# 请实现两个函数，分别用来序列化和反序列化二叉树
# 先序遍历，root->left->right

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Serialize(self, pRoot):
        serializeStr = ''
        if pRoot == None:
            return '#'
        stack = []
        while pRoot or stack:
            while pRoot:
                serializeStr += str(pRoot.val) + ','
                stack.append(pRoot)
                pRoot = pRoot.left
            serializeStr += '#,'
            pRoot = stack.pop()
            pRoot = pRoot.right
        serializeStr = serializeStr[:-1]
        return serializeStr

    def Deserialize(self, s):
        serialize = s.split(',')
        tree, sp = self.deserialize(serialize, 0)
        return tree

    def deserialize(self, s, sp):
        if sp >= len(s) or s[sp] == '#':
            return None, sp + 1
        node = TreeNode(int(s[sp]))
        sp += 1
        node.left, sp = self.deserialize(s, sp)
        node.right, sp = self.deserialize(s, sp)
        return node, sp


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
    ser = S.Serialize(root)
    print(ser)
    ser = S.Serialize(S.Deserialize(ser))
    print(ser)
