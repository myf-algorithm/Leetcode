class dlNode:
    def __init__(self, key, val, cnt=0):
        self.val = [key, val, cnt]
        self.pre = None
        self.nxt = None


class LFUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.c = capacity
        self.head = dlNode(1, 1, float('inf'))
        self.tail = dlNode(-1, -1, float('-inf'))
        self.head.nxt = self.tail
        self.tail.pre = self.head

    def _refresh(self, node, cnt):
        pNode, nNode = node.pre, node.nxt
        if cnt < pNode.val[2]:
            return
        pNode.nxt, nNode.pre = nNode, pNode
        while cnt >= pNode.val[2]:
            pNode = pNode.pre
        nNode = pNode.nxt
        pNode.nxt = nNode.pre = node
        node.pre, node.nxt = pNode, nNode

    def get(self, key: int) -> int:
        if self.c <= 0 or key not in self.cache:
            return -1
        node = self.cache[key]
        _, value, cnt = node.val
        node.val[2] = cnt + 1
        self._refresh(node, cnt + 1)
        return value

    def put(self, key: int, value: int) -> None:
        if self.c <= 0:
            return
        if key in self.cache:
            node = self.cache[key]
            _, _, cnt = node.val
            node.val = [key, value, cnt + 1]
            self._refresh(node, cnt + 1)
        else:
            if len(self.cache) >= self.c:
                tp, tpp = self.tail.pre, self.tail.pre.pre
                self.cache.pop(tp.val[0])
                tpp.nxt, self.tail.pre = self.tail, tpp
            node = dlNode(key, value)
            node.pre, node.nxt = self.tail.pre, self.tail
            self.tail.pre.nxt, self.tail.pre = node, node
            self.cache[key] = node
            self._refresh(node, 0)
