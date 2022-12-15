class Solution(object):
    def coinChange_dp(self, coins, amount):
        if amount == 0:
            return 0
        if amount < 0:
            return -1

        # 当目标金额为 i 时，至少需要 dp[i] 枚硬币凑出
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i - c] + 1)  # 1表示枚举的这枚硬币本身
                else:
                    continue
        return dp[-1] if dp[-1] != float('inf') else -1

    def coinChange_bfs(self, coins, amount):
        from collections import deque
        queue = deque([amount])
        step = 0
        visited = set()
        while queue:
            n = len(queue)
            for _ in range(n):
                tmp = queue.pop()
                if tmp == 0:
                    return step
                for coin in coins:
                    if tmp >= coin and tmp - coin not in visited:
                        visited.add(tmp - coin)
                        queue.appendleft(tmp - coin)
            step += 1
        return -1

    def coinChange_dfs(self, coins, amount):
        coins.sort(reverse=True)
        self.res = float('inf')

        def dfs(i, num, amount):
            if amount == 0:
                self.res = min(self.res, num)
                return
            for j in range(i, len(coins)):
                if (self.res - num) * coins[j] < amount:
                    break
                if coins[j] > amount:
                    continue
                dfs(j, num + 1, amount - coins[j])

        for i in range(len(coins)):
            dfs(i, 0, amount)
        return self.res if self.res != float('inf') else -1
