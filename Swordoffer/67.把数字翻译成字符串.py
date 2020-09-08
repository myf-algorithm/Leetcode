# 0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。
class Solution:
    def translateNum(self, num: int) -> int:
        str_num = str(num)
        n = len(str_num)
        dp = [1 for _ in range(n + 1)]
        for i in range(2, n + 1):
            if str_num[i - 2] == '1' or (str_num[i - 2] == '2' and str_num[i - 1] < '6'):
                dp[i] = dp[i - 2] + dp[i - 1]
            else:
                dp[i] = dp[i - 1]
        return dp[n]


#  有一种将字母编码成数字的方式：'a'->1, 'b->2', ... , 'z->26'。
class Solution_newcoder:
    def solve(self, nums):
        n = len(nums)
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        for i in range(1, n + 1):
            if i == 1:
                c = nums[i - 1]
                code1 = int(c)
                if 1 <= code1 <= 9:
                    dp[i] += dp[i - 1]
            else:
                c = nums[i - 1]
                cb = nums[i - 2]
                # back to 1:
                code1 = int(c)
                # back to 2:
                code2 = int(cb + c)
                if 1 <= code1 <= 9:
                    dp[i] += dp[i - 1]
                if 10 <= code2 <= 26:
                    dp[i] += dp[i - 2]
        return dp[-1]
