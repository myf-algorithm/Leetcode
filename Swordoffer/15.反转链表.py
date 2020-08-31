# -*- coding:utf-8 -*-
# 输入一个链表，反转链表后，输出新链表的表头。


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def ReverseList(self, pHead):
        head = None
        while pHead:
            tmp = ListNode(pHead.val)  # 使用当前位置的值创建一个新节点
            tmp.next = head  # 令新节点指向head，此时方向已经反过来了
            head = tmp  # 更新head为新节点
            pHead = pHead.next  # 移动到下一个位置
        return head

    # 递归首先找到新链表的头部节点，然后递归栈返回，层层反转
    # 首先找到新链表的头结点（即遍历到原链表的最后一个节点返回最后节点）
    # 执行函数体后续代码，将原链表中的尾节点指向原尾节点的前置节点
    # 前置节点的指针指向None（防止出现死循环）
    # 返回新链表的头部节点至上一层函数，重复以上操作
    def ReverseList_r(self, pHead):
        if pHead == None or pHead.next == None:
            return pHead
        p = self.ReverseList_r(pHead.next)
        pHead.next.next = pHead
        pHead.next = None
        return p

    def travel_list(self, pHead):  # 遍历链表，打印节点的值
        while pHead:
            print(pHead.val, end=' ')
            pHead = pHead.next


# 简洁写法
class Solution1:
    # 返回ListNode
    def ReverseList(self, pHead):
        pre, cur = None, pHead
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        return pre


if __name__ == '__main__':
    n0 = ListNode(0)
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n0.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    S = Solution()
    S.travel_list(S.ReverseList_r(n0))
