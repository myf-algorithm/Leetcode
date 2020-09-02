# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head:
            # ����ָ��Ѱ���м��
            slow, fast = head, head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            # �ָ�����
            insert = slow.next  # ȡ��
            slow.next = None  # �ض�

            # ��벿������ת
            cur_i, pre = insert, None
            while cur_i:
                tmp = cur_i.next
                cur_i.next = pre
                pre = cur_i
                cur_i = tmp

            # ����
            insert = pre  # preΪ��벿�ַ�ת���ͷ���
            cur1, cur2 = head, insert
            while cur2:
                tmp1 = cur1.next  # �ݴ���ಿ��
                cur1.next = None  # �ض�

                tmp2 = cur2.next  # �ݴ��Ҳಿ��
                cur2.next = None  # �ض�

                cur1.next = cur2  # ����
                cur1.next.next = tmp1  # ƴ��

                cur2 = tmp2  # �ָ�
                cur1 = cur1.next.next  # ����
