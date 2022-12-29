# -*- coding:utf-8 -*-
# 在一个二维数组中（每个一维数组的长度相同），
# 每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
# 请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。


class Solution:
    # 从右上角开始，大了往左，小了往下
    def Find(self, target, array):
        if len(array) == 0 or len(array[0]) == 0:
            return False
        i = 0  # i代表行
        j = len(array[0]) - 1  # j代表列
        while i < len(array) and j >= 0:
            if array[i][j] == target:
                return True
            elif array[i][j] > target:  # 当前位置的数值比目标词大，向左移动
                j = j - 1
            else:  # 当前位置的数值比目标词小，向下移动
                i = i + 1
        return False


class Solution1:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        cur_col = len(matrix[0]) - 1
        cur_row = 0
        while cur_col >= 0 and cur_row <= len(matrix) - 1:
            cur_num = matrix[cur_row][cur_col]
            if cur_num == target:
                return True
            if cur_num > target:
                cur_col -= 1
            if cur_num < target:
                cur_row += 1
        return False


if __name__ == '__main__':
    S = Solution()
    print(S.Find(3, [[1, 2], [3, 4]]))
