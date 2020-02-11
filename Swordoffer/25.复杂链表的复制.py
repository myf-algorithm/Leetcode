# -*- coding:utf-8 -*-
# 输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，
# 另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。
# （注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if pHead == None:
            return None
        # 复制节点在节点之后
        pCur = pHead
        while pCur != None:
            node = RandomListNode(pCur.label)
            node.next = pCur.next
            pCur.next = node
            pCur = node.next
        # 复制random节点
        pCur = pHead
        while pCur != None:
            if pCur.random != None:
                pCur.next.random = pCur.random.next
            pCur = pCur.next.next
        # 将新旧链表分离
        head = pHead.next
        cur = head
        pCur = pHead
        while pCur != None:
            pCur.next = pCur.next.next
            if cur.next != None:
                cur.next = cur.next.next
            cur = cur.next
            pCur = pCur.next
        return head

    def Clone_r(self, pHead):
        if not pHead: return
        newNode = RandomListNode(pHead.label)
        newNode.random = pHead.random
        newNode.next = self.Clone_r(pHead.next)
        return newNode


if __name__ == '__main__':
    S = Solution()
    root = RandomListNode(4)
    node0 = RandomListNode(2)
    node1 = RandomListNode(6)
    node2 = RandomListNode(1)
    node3 = RandomListNode(3)
    root.next = node0
    node1.next = node2
    node1.random = node3
    node2.next = node3
    S.Clone(root)
