# -*- coding:utf-8 -*-
# 给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
# 注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


# 分三种情况：
# a. 如果该结点存在右子结点，那么该结点的下一个结点是右子结点树上最左子结点
# b. 如果该结点不存在右子结点，且它是它父结点的左子结点，那么该结点的下一个结点是它的父结点
# c. 如果该结点既不存在右子结点，且也不是它父结点的左子结点，则需要一路向祖先结点搜索，
#    直到找到一个结点，该结点是其父亲结点的左子结点。如果这样的结点存在，
#    那么该结点的父亲结点就是我们要找的下一个结点。

class Solution:
    def GetNext(self, pNode):
        if pNode == None:
            return None
        # case a
        if pNode.right:
            tmp = pNode.right
            while (tmp.left):
                tmp = tmp.left
            return tmp
        p = pNode.next
        while (p and p.right == pNode):
            pNode = p
            p = p.next
        return p

if __name__ == "__main__":
    S = Solution()
    node = TreeLinkNode(1)
    node1 = TreeLinkNode(2)
    node2 = TreeLinkNode(3)
    node3 = TreeLinkNode(4)
    node.left = node1
    node.right = node2
    node.next = node3
    print(S.GetNext(node).val)
