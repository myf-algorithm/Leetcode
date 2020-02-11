# -*- coding:utf-8 -*-
# 输入一个链表，反转链表后，输出新链表的表头。


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def ReverseList(self, pHead):
        head = None
        while pHead:
            tmp = ListNode(pHead.val)
            tmp.next = head
            head = tmp
            pHead = pHead.next
        return head

    def ReverseList_r(self, pHead):
        if pHead == None or pHead.next == None:
            return pHead
        p = self.ReverseList_r(pHead.next)
        pHead.next.next = pHead
        pHead.next = None
        return p

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
    S = Solution()
    S.travel_list(S.ReverseList(n0))
