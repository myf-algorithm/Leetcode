# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        cur = dummy
        shi = ge = 0
        while l1 and l2:
            tmp_val = l1.val + l2.val + shi
            shi = tmp_val // 10
            tmp = ListNode(tmp_val % 10)
            cur.next = tmp
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        if l1:
            while l1:
                tmp_val = l1.val + shi
                shi = tmp_val // 10
                tmp = ListNode(tmp_val % 10)
                cur.next = tmp
                cur = cur.next
                l1 = l1.next
        if l2:
            while l2:
                tmp_val = l2.val + shi
                shi = tmp_val // 10
                tmp = ListNode(tmp_val % 10)
                cur.next = tmp
                cur = cur.next
                l2 = l2.next
        if shi == 1:
            tmp = ListNode(1)
            cur.next = tmp
        return dummy.next
