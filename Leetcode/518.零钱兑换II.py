class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        # dp[i][j]表示：从前 i 种硬币中凑出金额 j 的硬币组合数
        dp = [[0] * (amount + 1) for _ in range(n + 1)]  # 初始化
        dp[0][0] = 1  # 合法的初始化

        # 完全背包：优化后的状态转移
        for i in range(1, n + 1):  # 第一层循环：遍历硬币
            for j in range(amount + 1):  # 第二层循环：遍历背包
                if j < coins[i - 1]:  # 容量有限，无法选择第i个硬币
                    dp[i][j] = dp[i - 1][j]
                else:  # 可选择第i个硬币
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]

        return dp[n][amount]

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [0] * (amount + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            for j in range(amount + 1):
                if j >= coins[i - 1]:
                    dp[j] = dp[j] + dp[j - coins[i - 1]]

        return dp[amount]
