from collections import deque


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        q, res = [], []
        for i in range(len(nums)):
            if not q:  # 如果为空直接加入队列
                q.append(i)
            else:
                if i == q[0] + k:  # 如果队首的索引已位于滑动窗口之外，将其出队
                    q.pop(0)
                while q and nums[q[-1]] < nums[i]:  # 将小于当前值的队尾元素依次出队
                    q.pop()
                q.append(i)  # 将当前值加入队列
            res.append(nums[q[0]])  # 队首即最大值
        return res[k - 1:]  # k-1前不是有效的滑动窗口


import heapq


class Solution_heapq:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # 注意 Python 默认的优先队列是小根堆
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)  # 将列表转化为堆

        ans = [-q[0][0]]
        for i in range(k, n):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <= i - k:  # 最大值索引位于窗口左侧
                heapq.heappop(q)
            ans.append(-q[0][0])

        return ans


import collections


class Solution_deque:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = collections.deque()
        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)

        ans = [nums[q[0]]]
        for i in range(k, n):
            while q and nums[i] >= nums[q[-1]]:  # 将新的元素与队尾的元素相比较
                q.pop()  # 队尾的元素就可以被永久地移除
            q.append(i)
            while q[0] <= i - k:
                q.popleft()  # 从队首弹出元素，直到队首元素在窗口中为止
            ans.append(nums[q[0]])  # 由于队列中下标对应的元素是严格单调递减的，因此此时队首下标对应的元素就是滑动窗口中的最大值

        return ans
