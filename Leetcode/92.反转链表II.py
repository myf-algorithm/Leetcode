# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        dummy = ListNode(0)
        dummy.next = head
        a, d = dummy, dummy
        for _ in range(m - 1):
            a = a.next
        for _ in range(n):
            d = d.next
        b, c = a.next, d.next
        # o o o a b o o d c o o
        pre = b
        cur = pre.next
        while cur != c:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        a.next = d
        b.next = c
        return dummy.next
