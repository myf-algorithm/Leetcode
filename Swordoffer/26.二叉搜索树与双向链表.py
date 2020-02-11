# -*- coding:utf-8 -*-
# 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
# 要求不能创建任何新的结点，只能调整树中结点指针的指向。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.listHead = None
        self.listTail = None

    # 将二叉树转换为有序双向链表
    def Convert(self, pRootOfTree):
        if pRootOfTree == None:
            return
        # 主要思路是进行中序遍历
        self.Convert(pRootOfTree.left)
        if self.listHead == None:
            self.listHead = pRootOfTree
            self.listTail = pRootOfTree
        else:
            self.listTail.right = pRootOfTree
            pRootOfTree.left = self.listTail
            self.listTail = pRootOfTree  # 更新尾节点
        self.Convert(pRootOfTree.right)
        return self.listHead

    # 双向遍历双向链表
    def printList(self, listHead):
        while listHead.right:
            print(listHead.val, end=' ')
            listHead = listHead.right
        print(listHead.val)
        while listHead.left:
            print(listHead.val, end=' ')
            listHead = listHead.left
        print(listHead.val)


if __name__ == '__main__':
    S = Solution()
    root = TreeNode(4)
    node0 = TreeNode(2)
    node1 = TreeNode(6)
    node2 = TreeNode(1)
    node3 = TreeNode(3)
    node4 = TreeNode(5)
    node5 = TreeNode(7)
    root.left = node0
    root.right = node1
    node0.left = node2
    node0.right = node3
    node1.left = node4
    node1.right = node5
    S.printList(S.Convert(root))
