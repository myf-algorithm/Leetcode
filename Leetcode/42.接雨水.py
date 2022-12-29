from typing import List


class Solution:
    # 遍历，备忘录
    def trap1(self, height: List[int]) -> int:
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        left_max[0] = height[0]
        right_max[n - 1] = height[n - 1]

        for i in range(1, n):
            left_max[i] = max(height[i], left_max[i - 1])
        for i in range(n - 2, 0, -1):
            right_max[i] = max(height[i], right_max[i + 1])

        res = 0
        for i in range(1, n - 1):
            res += min(right_max[i], left_max[i]) - height[i]
        return res

    # 双指针
    def trap2(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        left_max = 0
        right_max = 0
        res = 0
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if left_max < right_max:
                res += (left_max - height[left])
                left += 1
            else:
                res += (right_max - height[right])
                right -= 1
        return res
