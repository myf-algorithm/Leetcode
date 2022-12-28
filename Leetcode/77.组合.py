class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, track = [], []

        def backtrack(n, start, k):
            # 结束条件，遍历到第k层时，开始收集当前结果track
            if len(track) == k:
                res.append(track[:])
                return

            for i in range(start, n):  # 选择列表是1到n之间的元素
                # 做选择
                track.append(i)

                # 递归
                backtrack(n, i + 1, k)

                # 撤销选择
                track.pop()

        backtrack(n + 1, 1, k)  # 选择列表是1到n之间的元素（包括n），所以start从1开始，到n+1结束
        return res