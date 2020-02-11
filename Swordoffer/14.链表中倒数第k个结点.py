# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        if head == None :
            return
        p1 = p2 = head
        for i in range(k):
            if p2 == None:
                return
            p2 = p2.next
        while p2:
            p2 = p2.next
            p1 = p1.next
        return p1


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
    print(S.FindKthToTail(n0, 2).val)