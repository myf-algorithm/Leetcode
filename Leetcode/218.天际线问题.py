import heapq

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []
        # 生成左右端点事件并排序
        for left, right, height in buildings:
            events.append([left, -height, right])
            events.append([right, 0, 0])
        events.sort()

        # 初始化结果与前序高度
        res = [[0, 0]]
        stack = [[0, float('inf')]]
        for left, height, right in events:
            # 超出管辖范围的先出队
            while left >= stack[0][1]:
                heapq.heappop(stack)
            # 加入备选天际线队列
            if height < 0:
                heapq.heappush(stack, [height, right])
            # 高度发生变化出现新的关键点
            if res[-1][1] != -stack[0][0]:
                res.append([left, -stack[0][0]])
        return res[1:]
