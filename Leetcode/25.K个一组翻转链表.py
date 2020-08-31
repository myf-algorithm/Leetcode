# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # ��ת k ��Ԫ�أ����ط�ת���ͷ��β�ڵ㡣
        def revrese(head, K):
            pre, cur = None, head
            for _ in range(K):
                tmp = cur.next
                cur.next = pre
                pre = pre, cur
                cur = tmp
            return pre, head

        pre = dummy = ListNode(0)
        dummy.next = head

        while pre.next:
            # �ж�ʣ��ڵ�����Ƿ��� k ������û��ֱ�ӷ��ء�
            # ��һ��Ŀ���ǽ� cur ��λ�� k+1 ���ڵ��λ�ã����������ƴ�ӡ�
            cur = pre.next
            for _ in range(k):
                if not cur:
                    return dummy.next
                cur = cur.next

            pre.next, pre = revrese(pre.next, k)  # �� pre �����Ѿ���ת�õ�Ԫ�أ�˳���ƶ� pre ��λ�á�
            pre.next = cur  # ƴ��ʣ��Ԫ�أ������޷�����������

        return dummy.next
