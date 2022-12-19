class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if (target + sum(nums)) % 2 != 0:
            return 0
        total = (target + sum(nums)) // 2  # 定义正数和为total
        if total < 0:  # 正数和为负，返回0
            return 0
        # dp[i][j]表示nums的前i个元素，和为j的的组合数
        dp = [[0 for _ in range(total + 1)] for _ in range(len(nums))]
        for j in range(total + 1):  # 初始化第一行
            if nums[0] == j:
                dp[0][j] = 1
        dp[0][0] += 1  # 初始化第一行后，[0][0]自增1，到此才算初始化结束

        for i in range(1, len(nums)):
            for j in range(total + 1):
                if j >= nums[i]:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]