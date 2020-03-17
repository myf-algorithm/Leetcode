# coding:utf-8
# 给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null


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

    def Loop(self):
        """链表尾部指向头"""
        if self.is_empty():
            self.__head = self.__head
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = self.__head

    def EntryNodeOfLoop(self):
        head = self.__head
        if head == None or head.next == None:
            return None
        slow = fast = head  # 初始化快慢指针，指向头结点
        while fast and fast.next:
            slow = slow.next  # 慢指针，每次移动一步
            fast = fast.next.next  # 快指针，每次移动两步
            if slow == fast:  # 快慢指针相遇，说明有环
                fast = head  # 将快指针置为头结点
                while fast != slow:
                    fast = fast.next  # 快指针，每次移动一步
                    slow = slow.next  # 慢指针，每次移动一步
                return fast  # 当快慢指针再次相遇时，快指针即为环的入口结点
        return None


if __name__ == "__main__":
    ll = SingleLinkList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.travel()
    ll.Loop()
    res = ll.EntryNodeOfLoop()
    print(res.elem)
