# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        if not (head and head.next):
            return True
        arr, i = [], 0
        # 申请一个数组，然后把元素都放到数组中
        while head:
            _, head = arr.append(head.val), head.next
        j = len(arr) - 1
        # 用i和j两个指针，一个往后，一个往前，不断迭代
        # 如果i的值不等于j说明不是回文，反之是回文
        while i < j:
            if arr[i] != arr[j]:
                return False
            i, j = i + 1, j - 1
        return True

    def isPalindrome_1(self, head):
        fast = slow = head
        # 快慢指针，快指针到达尾部，慢指针到达中间
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # 奇数长，fast指针在最后一个，slow在最中间，slow需要往后过一个
        # 偶数长，fast为空，slow指针中点过一个
        if fast:  # 奇数长的情况
            slow = slow.next
        pre = None
        cur = slow
        while cur:  # 反转后半部分链表
            tmp = cur.next
            cur.next = pre
            pre, cur = cur, tmp
        # pre为后半部分反转链表的头节点
        while pre and head:
            if pre.val != head.val:
                return False
            pre = pre.next
            head = head.next
        return True
