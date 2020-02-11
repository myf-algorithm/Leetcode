class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        分而治之
        """
        if not buildings:
            return []
        if len(buildings) == 1:
            return [[buildings[0][0], buildings[0][2]], [buildings[0][1], 0]]
        mid = len(buildings) // 2
        left = self.getSkyline(buildings[:mid])
        right = self.getSkyline(buildings[mid:])
        return self.merge(left, right)

    # 两个合并
    def merge(self, left, right):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        二分法
        """
        # 记录目前左右建筑物的高度
        lheight = rheight = 0
        # 位置
        l = r = 0
        # 输出结果
        res = []
        while l < len(left) and r < len(right):
            if left[l][0] < right[r][0]:
                # current point
                cp = [left[l][0], max(left[l][1], rheight)]
                lheight = left[l][1]
                l += 1
            elif left[l][0] > right[r][0]:
                cp = [right[r][0], max(right[r][1], lheight)]
                rheight = right[r][1]
                r += 1
            # 相等情况
            else:
                cp = [left[l][0], max(left[l][1], right[r][1])]
                lheight = left[l][1]
                rheight = right[r][1]
                l += 1
                r += 1
            # 和前面高度比较，不一样才加入
            if len(res) == 0 or res[-1][1] != cp[1]:
                res.append(cp)
        # 剩余部分添加进去
        res.extend(left[l:] or right[r:])
        return res

    def getSkyline_2div(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        二分法
        """
        import bisect
        res = [[0, 0]]
        # 记录 [left, height], [right, height]
        loc = []
        for l, r, h in buildings:
            # 为了排序让 left那边靠前, 所以让高度取负
            loc.append([l, -h])
            loc.append([r, h])
        loc.sort()
        heap = [0]

        for x, h in loc:
            if h < 0:
                bisect.insort(heap, h)
            else:
                heap.remove(-h)
            cur = -heap[0]
            if res[-1][1] != cur:
                res.append([x, cur])

        return res[1:]

    def getSkyline_heapq(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        堆
        """
        import bisect
        res = [[0, 0]]
        # 记录 [left, height], [right, height]
        loc = []
        for l, r, h in buildings:
            # 为了排序让 left那边靠前, 所以让高度取负
            loc.append([l, -h])
            loc.append([r, h])
        loc.sort()
        heap = [0]
        for x, h in loc:
            if h < 0:
                bisect.insort(heap, h)
            else:
                heap.remove(-h)
            cur = -heap[0]
            if res[-1][1] != cur:
                res.append([x, cur])
        return res[1:]





