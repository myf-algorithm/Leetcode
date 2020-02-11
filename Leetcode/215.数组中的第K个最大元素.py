import heapq


class Solution(object):
    def findKthLargest_heapq(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = [float('-inf') for i in range(k)]
        for i in nums:
            if i > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, i)
        return heap[0]

    def findKthLargest_2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        时间复杂度：遍历数组的复杂度为n，生成小数组的复杂度为k，二分查找的复杂度为logk，列表切片的复杂度为k，
                    因此综合时间复杂度为【k + n（logk + k）】。
        空间复杂度：小数组空间为k，每次列表切片操作的复杂度为k，因此总的空间复杂度为【（n + 1）k】
        """
        # 使用一个长度为k的小数组存储前k个元素（大小）
        # 遍历数组，使用二分法查找小数组中第一个比当前元素小的数
        ans = [float('-inf') for i in range(k)]
        for i in nums:
            # 如果当前元素小于等于数组中最小的元素
            if ans[0] >= i:
                continue
            # 如果当前元素大于等于数组中最大的元素
            if ans[-1] <= i:
                ans = ans[1:] + [i]
                continue
            # 二分法定位要插入的位置
            l = 0
            r = k - 1
            while l < r:
                m = (l + r) // 2
                # 如果i <= ans[m]，则需要插入的位置一定在m的左边，不包括m
                if i <= ans[m]:
                    r = m - 1
                # 如果i > ans[m]并且i小于m的下一个元素，则插入的位置在m
                elif i <= ans[m + 1]:
                    l = m
                    break
                # 插入的位置在m之后，不包括m
                else:
                    l = m + 1
            # 新的前k元素数组
            ans = ans[1:l + 1] + [i] + ans[l + 1:]
        return ans[0]

    def findKthLargest_quick_sort(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from random import randint

        # 改进的快排
        def quick_sort(left, right, nums):
            l, r = left, right
            index = randint(l, r)
            nums[l], nums[index] = nums[index], nums[l]
            while l < r:
                while l < r:
                    if nums[r] < nums[l]:
                        nums[l], nums[r] = nums[r], nums[l]
                        l += 1
                        while l < r:
                            if nums[l] > nums[r]:
                                nums[l], nums[r] = nums[r], nums[l]
                                r -= 1
                                break
                            else:
                                l += 1
                    else:
                        r -= 1
            if l == len(nums) - k:
                return nums[l]
            elif l > len(nums) - k:
                return quick_sort(left, l - 1, nums)
            else:
                return quick_sort(l + 1, right, nums)

        return quick_sort(0, len(nums) - 1, nums)
