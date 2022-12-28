class Solution(object):
    def permute(self, nums):
        res = []
        path = []
        used = []

        def backtrack(nums, used):
            if len(path) == len(nums):
                return res.append(path[:])
            for i in range(0, len(nums)):
                if nums[i] in used:
                    continue
                path.append(nums[i])
                used.append(nums[i])
                backtrack(nums, used)
                used.pop()
                path.pop()

        backtrack(nums, used)
        return res

    def permute1(self, nums):
        res = []
        path = []

        def backtrack(nums):
            if len(path) == len(nums):
                return res.append(path[:])
            for i in range(0, len(nums)):
                if nums[i] in path:
                    continue
                path.append(nums[i])
                backtrack(nums)
                path.pop()

        backtrack(nums)
        return res


if __name__ == '__main__':
    S = Solution()
    print(S.permute([1, 2, 3]))
