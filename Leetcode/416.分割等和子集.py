# leetcode 416 分割等和子集
from typing import List


class Solution:
    def canPartition2(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False
        total = sum(nums)
        maxNum = max(nums)

        if total & 1:
            return False

        target = total // 2
        if maxNum > target:
            return False

        # dp[i][j]表示：使用前i个物品，当前背包容量为j时，是否可以装满，可以为True
        dp = [[False] * (target + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = True

        dp[0][nums[0]] = True
        for i in range(1, n):
            num = nums[i]
            for j in range(1, target + 1):
                if j >= num:
                    # 不选取为dp[i - 1][j]，选取为dp[i - 1][j - num]
                    dp[i][j] = dp[i - 1][j] | dp[i - 1][j - num]
                else:
                    # 无法选取nums[i]
                    dp[i][j] = dp[i - 1][j]

        return dp[n - 1][target]

    def canPartition1(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False

        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        dp = [True] + [False] * target
        for i, num in enumerate(nums):
            for j in range(target, num - 1, -1):
                dp[j] |= dp[j - num]

        return dp[target]