# coding = utf-8

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head, x):
        if not head or not head.next:
            return head
        head1 = ListNode(0)
        cur1 = head1
        head2 = ListNode(0)
        cur2 = head2
        cur = head
        while cur:
            if cur.val < x:
                cur1.next = cur
                cur1 = cur1.next
            else:
                cur2.next = cur
                cur2 = cur2.next
            cur = cur.next
        cur1.next = head2.next
        cur2.next = None
        return head1.next
