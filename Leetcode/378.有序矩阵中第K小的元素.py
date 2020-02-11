class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # 计算小于等于目标值的元素个数，根据递增原则，从右上角开始查找
        def count_num(m, target):
            i = 0
            j = len(m) - 1
            ans = 0
            while i < len(m) and j >= 0:
                if m[i][j] <= target:
                    ans += j + 1
                    i += 1
                else:
                    j -= 1
            return ans

        #  思路：左上角元素最小，右下角元素最大，计算小于等于中间值的元素个数
        left = matrix[0][0]
        right = matrix[-1][-1]
        # 二分法查找
        while left < right:
            mid = (left + right) >> 1
            count = count_num(matrix, mid)
            if count < k:
                left = mid + 1
            else:
                right = mid
        return left
