# coding:utf-8
# 在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，
# 重复的结点不保留，返回链表头指针。
# 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5


class Node(object):
    """节点"""

    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleLinkList(object):
    """单链表"""

    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head == None

    def length(self):
        """链表长度"""
        # cur游标，用来移动遍历节点
        cur = self.__head
        # count记录数量
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        while cur != None:
            print(cur.elem, end=" ")
            cur = cur.next
        print("")

    def add(self, item):
        """链表头部添加元素，头插法"""
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        """链表尾部添加元素, 尾插法"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        """指定位置添加元素
           pos 从0开始
        """
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            pre = self.__head
            count = 0
            while count < (pos - 1):
                count += 1
                pre = pre.next
            # 当循环退出后，pre指向pos-1位置
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """删除节点"""
        cur = self.__head
        pre = None
        while cur != None:
            if cur.elem == item:
                # 先判断此结点是否是头节点
                # 头节点
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        """查找节点是否存在"""
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False

    def get_head(self):
        return self.__head


class Solution:
    def deleteDuplication(self, pHead):
        if pHead == None or pHead.next == None:
            return pHead
        dummy = Node(0)  # 保留头结点，最后返回dummy.next
        dummy.next = pHead
        pre = dummy
        cur = dummy.next

        # 使用前后指针，进行移动遍历
        while cur != None:
            # 更新后指针
            while cur.next and cur.next.elem == pre.next.elem:
                cur = cur.next

            # 更新前指针
            if pre.next == cur:  # 对应没有相邻重复元素的情况
                pre = pre.next
            else:  # 对应具有相邻重复元素，已经进行过移位
                pre.next = cur.next  # 跳过重复元素

            # 更新后指针
            cur = cur.next
        return dummy.next


if __name__ == "__main__":
    ll = SingleLinkList()
    ll.append(1)
    ll.append(1)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.travel()

    S = Solution()
    ll_res = SingleLinkList(S.deleteDuplication(ll.get_head()))
    ll_res.travel()
