import collections


class Node:
    def __init__(self, keys=collections.deque(), count=0):
        self.keys = keys
        self.count = count
        self.left = None
        self.right = None

    def insert(self, new):
        new.right = self.right
        new.left = self
        new.right.left = new
        new.left.right = new

    def remove(self):
        self.left.right = self.right
        self.right.left = self.left


class LFUCache:
    def __init__(self, capacity: int):
        self.memo = {}
        self.kv = {}
        self.root = Node()
        self.root.right = self.root
        self.root.left = self.root
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.kv:
            return -1
        res = self.kv[key]
        if self.memo[key].right.count == self.memo[key].count + 1:
            self.memo[key].right.keys.append(key)
        else:
            new = Node(keys=collections.deque([key]), count=self.memo[key].count + 1)
            self.memo[key].insert(new)

        tmp = self.memo[key].right

        self.memo[key].keys.remove(key)
        if not self.memo[key].keys:
            self.memo[key].remove()
        self.memo[key] = tmp
        return res

    def put(self, key: int, value: int) -> None:
        if key not in self.kv:
            if len(self.kv) == self.cap:
                to_pop = self.root.right.keys.popleft()
                if not self.root.right.keys:
                    self.root.right.remove()
                self.kv.pop(to_pop)
                self.memo.pop(to_pop)

            self.kv[key] = value
            if self.root.right.count == 1:
                self.root.right.keys.append(key)
            else:
                new = Node(keys=collections.deque([key]), count=1)
                self.root.insert(new)

            self.memo[key] = self.root.right

        else:
            self.get(key)
            self.kv[key] = value
