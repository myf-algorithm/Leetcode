class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums)

        # 基本情况
        if 1 not in nums:
            return 1

        # nums = [1]
        if n == 1:
            return 2

        # 用1替换负数，0和大于n的数，在转换以后，nums只会包含正数
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1

        # 使用索引和数字符号作为检查器
        # 例如，如果 nums[1] 是负数表示在数组中出现了数字 `1`
        # 如果 nums[2] 是正数 表示数字 2 没有出现
        for i in range(n):
            a = abs(nums[i])
            # 如果发现了一个数字a，改变第a个元素的符号
            # 注意重复元素只需操作一次
            if a == n:
                nums[0] = -abs(nums[0])
            else:
                nums[a] = -abs(nums[a])

        # 现在第一个正数的下标，就是第一个缺失的数
        for i in range(1, n):
            if nums[i] > 0:
                return i

        if nums[0] > 0:
            return n

        return n + 1

    def firstMissingPositive1(self, nums):
        if not nums:
            return 1
        i = 1
        while True:
            if i in nums:
                i += 1
            else:
                return i


if __name__ == '__main__':
    S = Solution()
    print(S.firstMissingPositive([1, 2, 0]))
