# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def Merge(self, pHead1, pHead2):
        res = ListNode(0)  # 定义初始节点
        tmp = res  # 定义遍历节点
        p1 = pHead1
        p2 = pHead2
        while p1 and p2:
            if p1.val < p2.val:  # 如果p1的值小于p2的值
                tmp.next = p1
                p1 = p1.next
            else:  # 如果p1的值大于等于p2的值
                tmp.next = p2
                p2 = p2.next
            tmp = tmp.next
        if p1:
            tmp.next = p1
        if p2:
            tmp.next = p2
        return res.next

    def travel_list(self, pHead):
        while pHead:
            print(pHead.val, end=' ')
            pHead = pHead.next


if __name__ == '__main__':
    n0 = ListNode(0)
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n0.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4

    m0 = ListNode(0)
    m1 = ListNode(1)
    m2 = ListNode(2)
    m3 = ListNode(3)
    m4 = ListNode(4)
    m0.next = m1
    m1.next = m2
    m2.next = m3
    m3.next = m4

    S = Solution()
    S.travel_list(n0)
    S.travel_list(pHead=S.Merge(n0, m0))
