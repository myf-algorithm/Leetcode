class Solution:
    # # 最原始解法，时间超出限制
    # def twoSum(nums, target):
    #     result = [0, 0]
    #     i = j = 0
    #     l = len(nums)
    #     while i < l - 1:
    #         j = i + 1
    #         while j < l:
    #             if nums[i] + nums[j] == target:
    #                 result = [i, j]
    #             j = j + 1
    #         i = i + 1
    #     return result

    # # 暴力解法 7720ms
    # def twoSum(self, nums, target):
    #     for i in range(len(nums) - 1):
    #         for j in range(i + 1, len(nums)):
    #             if nums[i] + nums[j] == target:
    #                 return [i, j]

    # # 字典方法 56ms
    # def twoSum(nums, target):
    #     keys = {}
    #     for i in range(len(nums)):
    #         if nums[i] in keys:
    #             return [keys[nums[i]], i]
    #         if nums[i] not in keys:
    #             keys[target - nums[i]] = i

    # # 字典方法 48ms
    # def twoSum(nums, target):
    #     keys = {}
    #     for i in range(len(nums)):
    #         comp = target - nums[i]
    #         if comp in keys:
    #             return [keys[comp], i]
    #         keys[nums[i]] = i

    # # 字典方法 44ms 原理同上
    # def twoSum(nums, target):
    #     keys = {}
    #     for i in range(len(nums)):
    #         if ((target - nums[i]) in keys):
    #             return [keys[target - nums[i]], i]
    #         if (nums[i] not in keys):
    #             keys[nums[i]] = i

    # 字典方法 36ms
    def twoSum(self, nums, target):
        keys = {}
        for i, n in enumerate(nums):
            if target - n in keys:
                return [keys[target - n], i]
            keys[n] = i


nums = [1, 2, 5, 6]
target = 7
S = Solution()  # 实例化对象
print(S.twoSum(nums, target))
for i, num in enumerate(nums):
    print(str(i) + ' ' + str(num))


