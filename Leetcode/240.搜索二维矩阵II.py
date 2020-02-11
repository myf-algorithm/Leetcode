class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        row = len(matrix)
        col = len(matrix[0])
        i = 0
        j = col - 1  # 从右上角元素开始
        while i < row and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:  # 如果当前元素值大于target，列号减1
                j -= 1
            else:  # 如果当前元素值小于target，行号加1
                i += 1
        return False

    def searchMatrix1(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        m, n = len(matrix), len(matrix[0])
        i, j = 0, 0
        while i < m and j < n:
            # 判断行
            if matrix[i][j] <= target <= matrix[i][n - 1]:
                s, e = j, n
                while e - s > 1:
                    mid = (s + e) // 2
                    if matrix[i][mid] == target:
                        return True
                    elif matrix[i][mid] < target:
                        s = mid
                    else:
                        e = mid
                else:
                    if matrix[i][s] == target or matrix[i][e] == target:
                        return True
            if matrix[i][j] <= target <= matrix[m - 1][j]:
                s, e = i, m
                while e - s > 1:
                    mid = (s + e) // 2
                    if matrix[mid][j] == target:
                        return True
                    elif matrix[mid][j] < target:
                        s = mid
                    else:
                        e = mid
                else:
                    if matrix[s][j] == target or matrix[e][j] == target:
                        return True
            i += 1
            j += 1
        return False
