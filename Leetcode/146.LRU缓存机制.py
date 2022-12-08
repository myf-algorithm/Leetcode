# 运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。
# 它应该支持以下操作： 获取数据 get 和 写入数据 put 。
#
# 获取数据 get(key) - 如果关键字 (key) 存在于缓存中，则获取关键字的值（总是正数），否则返回 -1。
# 写入数据 put(key, value) -
#                   如果关键字已经存在，则变更其数据值；
#                   如果关键字不存在，则插入该组「关键字/值」。
#                   当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，
#                   从而为新的数据值留出空间。

# 数据结构：
# 双向链表按照被使用的顺序存储了这些键值对，靠近头部的键值对是最近使用的，而靠近尾部的键值对是最久未使用的
# 哈希表即为普通的哈希映射（HashMap），通过缓存数据的键映射到其在双向链表中的位置

# 算法逻辑：
# 对于 get 操作，首先判断 key 是否存在：
# 如果 key 不存在，则返回 −1；
# 如果 key 存在，则 key 对应的节点是最近被使用的节点。通过哈希表定位到该节点在双向链表中的位置，并将其移动到双向链表的头部，最后返回该节点的值。

# 对于 put 操作，首先判断 key 是否存在：
# 如果 key 不存在，使用 key 和 value 创建一个新的节点，在双向链表的头部添加该节点，并将 key 和该节点添加进哈希表中。然后判断双向链表的节点数是否超出容量，如果超出容量，则删除双向链表的尾部节点，并删除哈希表中对应的项；
# 如果 key 存在，则与 get 操作类似，先通过哈希表定位，再将对应的节点的值更新为 value，并将该节点移到双向链表的头部。


class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.hashmap = {}

        # 新建两个节点head和tail
        self.head = ListNode()
        self.tail = ListNode()

        # 初始化链表为head <-> tail
        self.head.next = self.tail
        self.tail.prev = self.head

    # 定义方法将任一个节点移动到双向链表末尾
    def move_node_to_tail(self, key):
        # 先将哈希表key指向的节点拎出来，为了简洁起名node
        #      hashmap[key]                               hashmap[key]
        #           |                                          |
        #           V              -->                         V
        # prev <-> node <-> next         pre <-> next   ...   node
        node = self.hashmap[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        # 之后将node插入到尾节点前
        #                 hashmap[key]                 hashmap[key]
        #                      |                            |
        #                      V        -->                 V
        # prev <-> tail  ...  node                prev <-> node <-> tail
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.hashmap:
            # 如果已经在链表中了就把它移动到末尾(变成最新访问的)
            self.move_node_to_tail(key)
        res = self.hashmap.get(key, -1)
        if res == -1:
            return res
        else:
            return res.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.hashmap:
            # 如果key本身已经在哈希表中了就不需要在链表中加入新的节点
            # 但是需要更新字典该值对应节点的val
            self.hashmap[key].value = value
            # 之后将该节点移动到末尾
            self.move_node_to_tail(key)
        else:
            if len(self.hashmap) == self.capacity:
                # 去掉哈希表对应项
                self.hashmap.pop(self.head.next.key)
                # 去掉最久没有被访问过的节点，即头节点之后的节点
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
            # 如果不在的话就插入到尾节点前
            new = ListNode(key, value)
            self.hashmap[key] = new
            new.prev = self.tail.prev
            new.next = self.tail
            self.tail.prev.next = new
            self.tail.prev = new


import collections


class LRUCache_easy(collections.OrderedDict):
    def __init__(self, capacity: int):
        super().__init__()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.put(1, 2)
param_1 = obj.get(1)
obj.put(1, 2)
print(param_1)
