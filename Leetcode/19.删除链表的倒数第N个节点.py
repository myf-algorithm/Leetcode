# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        p = dummy
        p.next = head
        i = 0
        while p:
            p = p.next
            i += 1

        p = self.head
        t = 0
        while True:
            if t == i - n - 1:
                p.next = p.next.next
                return self.head.next
            p = p.next
            t += 1

    def removeNthFromEnd_doublePoint(self, head: ListNode, n: int) -> ListNode:
        a = ListNode(0)
        a.next = head
        p = q = a
        i = 0
        while i < n:
            p = p.next
            i += 1
        while p.next:
            p = p.next
            q = q.next
        q.next = q.next.next
        return a.next

    def removeNthFromEnd_slowfast(self, head: ListNode, n: int) -> ListNode:
        slow = head
        fast = head
        for i in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        if slow.next.next:
            slow.next = slow.next.next
        else:
            slow.next = None
        return head


def generateList(l: list) -> ListNode:
    prenode = ListNode(0)
    lastnode = prenode
    for val in l:
        lastnode.next = ListNode(val)
        lastnode = lastnode.next
    return prenode.next


def printList(l: ListNode):
    while l:
        print("%d, " % (l.val), end='')
        l = l.next
    print('')


if __name__ == '__main__':
    s = Solution()
    l1 = generateList([1, 2, 3, 4, 5])
    printList(s.removeNthFromEnd_doublePoint(l1, 2))
