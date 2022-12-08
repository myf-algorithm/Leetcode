import heapq


class MedianFinder:
    def __init__(self):
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        if not self.minheap or num <= -self.minheap[0]:  # 如果之前为空或者当前要进来的元素比minheap最大的元素还小
            heapq.heappush(self.minheap, -num)
            if len(self.minheap) > len(self.maxheap) + 1:  # 如果minheap队列比另一个长度大1以上，则应该把一个元素拿出来放到另一个队列中
                heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))
        else:
            heapq.heappush(self.maxheap, num)
            if len(self.maxheap) > len(self.minheap) + 1:  # # 如果maxheap队列比另一个长度大1以上，则应该把一个元素拿出来放到另一个队列中
                heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))

    def findMedian(self) -> float:
        if len(self.minheap) == len(self.maxheap):
            return (-self.minheap[0] + self.maxheap[0]) / 2
        elif len(self.minheap) > len(self.maxheap):
            return -self.minheap[0]
        else:
            return self.maxheap[0]
