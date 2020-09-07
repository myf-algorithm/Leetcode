#  例如：给定的候选数集是[10,1,2,7,6,1,5]，目标数是8
# 解集是：
# [1, 7]
# [1, 2, 5]
# [2, 6]
# [1, 1, 6]


class Solution:
    def combinationSum2(self, num, target):
        num.sort()

        def dfs(start, num, path, res, target):
            if target == 0:
                res.append(path[:])
                return
            for i in range(start, len(num)):
                if num[i] <= target:
                    if i > start and num[i] == num[i - 1]:
                        continue
                    path.append(num[i])
                    dfs(i + 1, num, path, res, target - num[i])
                    path.pop()

        start = 0
        path = []
        res = []
        dfs(start, num, path, res, target)
        return res
