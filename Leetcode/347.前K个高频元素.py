class Solution(object):
    def topKFrequent_Counter(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter
        return [i[0] for i in Counter(nums).most_common(k)]

    def topKFrequent_Heap_Counter(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter
        import heapq
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)

    def topKFrequent_Heap(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        def heapify(arr, n, i):
            smallest = i  # 构造根节点与左右子节点
            l = 2 * i + 1
            r = 2 * i + 2
            if l < n and arr[l][1] < arr[i][1]:  # 如果左子节点在范围内且小于父节点
                smallest = l
            if r < n and arr[r][1] < arr[smallest][1]:
                smallest = r
            if smallest != i:  # 递归基:如果没有交换，退出递归
                arr[i], arr[smallest] = arr[smallest], arr[i]
                heapify(arr, n, smallest)  # 确保交换后，小于其左右子节点

        # 哈希字典统计出现频率
        map_dict = {}
        for item in nums:
            if item not in map_dict.keys():
                map_dict[item] = 1
            else:
                map_dict[item] += 1

        map_arr = list(map_dict.items())
        lenth = len(map_dict.keys())
        # 构造规模为k的minheap
        if k <= lenth:
            k_minheap = map_arr[:k]
            # 从后往前建堆，避免局部符合而影响递归跳转，例:2,1,3,4,5,0
            for i in range(k // 2 - 1, -1, -1):
                heapify(k_minheap, k, i)
            # 对于k:, 大于堆顶则入堆，维护规模为k的minheap
            for i in range(k, lenth):  # 堆建好了，没有乱序，从前往后即可
                if map_arr[i][1] > k_minheap[0][1]:
                    k_minheap[0] = map_arr[i]  # 入堆顶
                    heapify(k_minheap, k, 0)  # 维护 minheap
        # 如需按顺序输出，对规模为k的堆进行排序
        # 从尾部起，依次与顶点交换再构造minheap，最小值被置于尾部
        for i in range(k - 1, 0, -1):
            k_minheap[i], k_minheap[0] = k_minheap[0], k_minheap[i]
            k -= 1  # 交换后，维护的堆规模-1
            heapify(k_minheap, k, 0)
        return [item[0] for item in k_minheap]
