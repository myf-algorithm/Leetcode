# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:  # 递归终止条件
            return head
        slow, fast = head, head.next  # 使用快慢指针寻找中间节点
        while fast and fast.next:  # 奇数个节点找到中点，偶数个节点找到中心左边的节点
            fast, slow = fast.next.next, slow.next
        mid, slow.next = slow.next, None  # 中点为slow，将链表切断
        left, right = self.sortList(head), self.sortList(mid)  # 分割环节

        h = res = ListNode(0)  # 建立h为头部
        while left and right:
            if left.val < right.val:  # 从小到大进行合并
                h.next, left = left, left.next
            else:
                h.next, right = right, right.next
            h = h.next
        h.next = left if left else right
        return res.next

    def sortList_iter(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        h, length, intv = head, 0, 1
        while h:
            h, length = h.next, length + 1
        res = ListNode(0)
        res.next = head
        # 多轮排序合并
        while intv < length:
            pre, h = res, res.next
            while h:  # 代表此轮intv合并完成，跳出
                # 找到合并单元1的头部h1
                h1, i = h, intv
                while i and h:
                    h, i = h.next, i - 1
                if i:
                    break
                # 找到合并单元2的头部h2
                h2, i = h, intv
                while i and h:
                    h, i = h.next, i - 1
                c1, c2 = intv, intv - i

                while c1 and c2:  # 合并长度为c1, c2的h1, h2链表
                    if h1.val < h2.val:
                        pre.next, h1, c1 = h1, h1.next, c1 - 1
                    else:
                        pre.next, h2, c2 = h2, h2.next, c2 - 1
                    pre = pre.next
                pre.next = h1 if c1 else h2
                while c1 > 0 or c2 > 0:
                    pre, c1, c2 = pre.next, c1 - 1, c2 - 1
                pre.next = h  # 合并单元尾部同时也作为下次合并的辅助头部
            intv *= 2  # 切换到下轮合并
        return res.next
