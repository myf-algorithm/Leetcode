# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

    def hasCycle_set(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        hash_set = set()
        while head:
            if head in hash_set:
                return True
            hash_set.add(head)
            head = head.next
        return False

    def hasCycle_none(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        while head.next and head.val != None:
            head.val = None  # 遍历的过程中将值置空
            head = head.next
        if not head.next:  # 如果碰到空发现已经结束，则无环
            return False
        return True  # 否则有环
