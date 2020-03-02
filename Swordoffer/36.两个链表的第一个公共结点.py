# -*- coding:utf-8 -*-
# 输入两个链表，找出它们的第一个公共结点。


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        if pHead1 == None or pHead2 == None:
            return None
        p1, p2 = pHead1, pHead2
        # 因为是公共节点，所以可以把这两个链表拼成两个不同的链表
        # 同时遍历这两个链表，经过(m+n)次迭代之后肯定能找到公共节点
        while p1 != p2:
            p1 = pHead2 if p1 is None else p1.next
            p2 = pHead1 if p2 is None else p2.next
        return p1


if __name__ == '__main__':
    a0 = ListNode(1)
    a1 = ListNode(2)
    a2 = ListNode(3)
    a3 = ListNode(4)
    a4 = ListNode(5)
    a0.next = a1
    a1.next = a2
    a2.next = a3
    a3.next = a4

    b0 = ListNode(6)
    b1 = ListNode(7)
    b0.next = b1
    b1.next = a2
    a2.next = a3
    a3.next = a4

    S = Solution()
    print(S.FindFirstCommonNode(a0, b0).val)
