# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        l1 = head
        l2 = head.next
        cur = l2
        while l1 and l2 and l1.next.next and l2.next:
            l1.next = l1.next.next
            l2.next = l2.next.next
            l1 = l1.next
            l2 = l2.next
        l1.next = cur
        return head

