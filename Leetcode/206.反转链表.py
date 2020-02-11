# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        new_head = None
        while head:
            tmp = head.next
            head.next = new_head
            new_head = head
            head = tmp
        return new_head

    def reverseList_r(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        next_node = head.next
        res = self.reverseList(next_node)
        # 将头节点接到反转链表的尾部
        next_node.next = head
        head.next = None
        return res


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
    printList(s.reverseList(l1))
