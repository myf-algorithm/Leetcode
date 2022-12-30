# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def revrese(head, K):
            pre, cur = None, head
            for _ in range(K):
                cur.next, pre, cur = pre, cur, cur.next
            return pre, head

        pre = dummy = ListNode(0)
        dummy.next = head

        while pre.next:
            cur = pre.next
            for _ in range(k):
                if not cur:
                    return dummy.next
                cur = cur.next

            pre.next, pre = revrese(pre.next, k)
            pre.next = cur

        return dummy.next
