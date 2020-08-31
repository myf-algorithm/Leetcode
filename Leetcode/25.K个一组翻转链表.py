# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        pass


    # ��תk��Ԫ�أ����ط�ת���ͷβ�ڵ�
    def reverse(self, head, k):
        pre, cur = None, head
        for _ in range(k):
            cur.next = pre
            pre = cur
            cur = cur.next
        return pre
