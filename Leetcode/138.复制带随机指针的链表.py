"""
# Definition for a Node.
"""


class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList_dfs(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        lookup = {}

        def dfs(head):
            if not head:
                return None
            if head in lookup:
                return lookup[head]
            clone = Node(head.val, None, None)
            lookup[head] = clone
            clone.next, clone.random = dfs(head.next), dfs(head.random)
            return clone

        return dfs(head)

    def copyRandomList_bfs(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        from collections import deque
        lookup = {}

        def bfs(head):
            if not head:
                return head
            clone = Node(head.val, None, None)
            queue = deque()
            queue.appendleft(head)
            lookup[head] = clone
            while queue:
                tmp = queue.pop()
                if tmp.next and tmp.next not in lookup:
                    lookup[tmp.next] = Node(tmp.next.val, [], [])
                    queue.appendleft(tmp.next)
                if tmp.random and tmp.random not in lookup:
                    lookup[tmp.random] = Node(tmp.random.val, [], [])
                    queue.appendleft(tmp.random)
                lookup[tmp].next = lookup.get(tmp.next)
                lookup[tmp].random = lookup.get(tmp.random)
            return clone

        return bfs(head)

    def copyRandomList_node(self, head):
        if not head:
            return None
        lookup = {}
        node = head
        # 创建所有节点
        while node:
            lookup[node] = Node(node.val, None, None)
            node = node.next

        node = head
        # 节点连接
        while node:
            lookup[node].next = lookup.get(node.next)
            lookup[node].random = lookup.get(node.random)
            node = node.next
        return lookup[head]

    def copyRandomList_copy(self, head):
        if not head:
            return None
        # 复制节点
        cur = head
        while cur:
            # 保存下一个节点
            tmp = cur.next
            # 后面跟着同样的节点
            cur.next = Node(cur.val, None, None)
            # 拼接
            cur.next.next = tmp
            cur = tmp
        # 复制random指针
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        # 拆分
        cur = head
        copy_head = head.next
        copy_cur = copy_head
        while copy_cur.next:
            # 组head
            cur.next = cur.next.next
            cur = cur.next
            # 组 copy_head
            copy_cur.next = copy_cur.next.next
            copy_cur = copy_cur.next
        # 把链表结束置空
        cur.next = copy_cur.next
        copy_cur.next = None
        return copy_head
