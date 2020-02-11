# -*- coding:utf-8 -*-
# 堆是一种完全二叉树，完全二叉树是一种除了最后一层之外的其他每一层都被完全填充，并且所有结点都保持向左对齐的树
# 堆有两种类型: 大根堆 小根堆
# 大根堆：所有的父节点的值都比孩子节点大，叶子节点值最小，root根节点是第一个节点值最大
# 小根堆：和大顶堆相反，所有父节点值，都小于子节点值，root根节点是第一个节点值最小

"""
    Heaps:
    完全二叉树，最大堆的非叶子节点的值都比孩子大，最小堆的非叶子结点的值都比孩子小
    Heap包含两个属性，order property 和 shape property(a complete binary tree)，在插入
    一个新节点的时候，始终要保持这两个属性
    插入操作：保持堆属性和完全二叉树属性, sift-up 操作维持堆属性
    extract操作：只获取根节点数据，并把树最底层最右节点copy到根节点后，sift-down操作维持堆属性
    用数组实现heap，从根节点开始，从上往下从左到右给每个节点编号，则根据完全二叉树的
    性质，给定一个节点i， 其父亲和孩子节点的编号分别是:
        parent = (i-1) // 2
        left = 2 * i + 1
        rgiht = 2 * i + 2
    使用数组实现堆一方面效率更高，节省树节点的内存占用，一方面还可以避免复杂的指针操作，减少调试难度。
    """


class MaxHeap(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self._elements = [0] * maxsize
        self._count = 0

    def __len__(self):
        return self._count

    def add(self, value):
        if self._count >= self.maxsize:
            raise Exception('full')
        self._elements[self._count] = value
        self._count += 1
        self._siftup(self._count - 1)  # 维持堆的特性

    def _siftup(self, ndx):
        if ndx > 0:
            parent = int((ndx - 1) / 2)
            if self._elements[ndx] > self._elements[parent]:  # 如果插入的值大于 parent，一直交换
                self._elements[ndx], self._elements[parent] = self._elements[parent], self._elements[ndx]
                self._siftup(parent)  # 递归

    def extract(self):
        if self._count <= 0:
            raise Exception('empty')
        value = self._elements[0]  # 保存 root 值
        self._count -= 1
        self._elements[0] = self._elements[self._count]  # 最右下的节点放到root后siftDown
        self._siftdown(0)  # 维持堆特性
        return value

    def _siftdown(self, ndx):
        left = 2 * ndx + 1
        right = 2 * ndx + 2
        # determine which node contains the larger value
        largest = ndx
        if (left < self._count and  # 有左孩子
                self._elements[left] >= self._elements[largest] and
                self._elements[left] >= self._elements[right]):  # 原书这个地方没写实际上找的未必是largest
            largest = left
        elif right < self._count and self._elements[right] >= self._elements[largest]:
            largest = right
        if largest != ndx:
            self._elements[ndx], self._elements[largest] = self._elements[largest], self._elements[ndx]
            self._siftdown(largest)


def test_maxheap():
    import random
    n = 5
    h = MaxHeap(n)
    for i in range(n):
        h.add(i)
    for i in reversed(range(n)):
        assert i == h.extract()


def heapsort_reverse(array):
    length = len(array)
    maxheap = MaxHeap(length)
    for i in array:
        maxheap.add(i)
    res = []
    for i in range(length):
        res.append(maxheap.extract())
    return res


def test_heapsort_reverse():
    import random
    l = list(range(10))
    random.shuffle(l)
    # assert heapsort_reverse(l) == sorted(l, reverse=True)
    return heapsort_reverse(l)


def heapsort_use_heapq(iterable):
    from heapq import heappush, heappop
    items = []
    for value in iterable:
        heappush(items, value)
    return [heappop(items) for i in range(len(items))]


def test_heapsort_use_heapq():
    import random
    l = list(range(10))
    random.shuffle(l)
    # assert heapsort_use_heapq(l) == sorted(l)
    return heapsort_use_heapq(l)


if __name__ == '__main__':
    test_maxheap()
    print(test_heapsort_reverse())
    print(test_heapsort_use_heapq())
