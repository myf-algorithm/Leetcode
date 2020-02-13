# -*- coding:utf-8 -*-
# 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
# 输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。
# 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
# NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。


class Solution:
    # 辅助函数，寻找rotateArray中，从left到right的最小值
    def MininOrder(self, rotateArray, left, right):
        res = rotateArray[left]
        for i in range(left, right + 1):
            if res > rotateArray[i]:
                res = rotateArray[i]

    def minNumberInRotateArray(self, rotateArray):
        lenArr = len(rotateArray)
        left, right = 0, lenArr - 1
        while left <= right:
            if right - left == 1:
                return rotateArray[right]   # 下标相差为1时，直接输出右值
            mid = (left + right) // 2
            if rotateArray[left] == rotateArray[mid] and rotateArray[mid] == rotateArray[right]:
                return self.MininOrder(rotateArray, left, right)  # 无法判断最小值在那一边，进行暴力查找
            if rotateArray[mid] >= rotateArray[left]:  # 中间值大于左值，最小值在右边，2345671，5>2
                left = mid
            elif rotateArray[mid] <= rotateArray[right]:  # 中间值小于右值，最小值在左边，5671234，1<4
                right = mid
        return rotateArray[right]


if __name__ == '__main__':
    S = Solution()
    list = [5, 6, 7, 1, 2, 3, 4]
    print(S.minNumberInRotateArray(list))
