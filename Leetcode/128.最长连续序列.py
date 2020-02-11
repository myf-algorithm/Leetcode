class Solution(object):
    def longestConsecutive(self, nums):  # 哈希表和线性空间的构造
        """
        :type nums: List[int]
        :rtype: int
        """
        longest_streak = 0
        num_set = set(nums)  # {1, 2, 3, 100, 4, 200}
        print(num_set)
        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                longest_streak = max(longest_streak, current_streak)
        return longest_streak

    def longestConsecutive_sort(self, nums):  # 先进行排序
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        nums.sort()
        longest_streak = 1
        current_streak = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i - 1] + 1:
                    current_streak += 1
                else:
                    longest_streak = max(longest_streak, current_streak)
                    current_streak = 1

        return max(longest_streak, current_streak)


if __name__ == '__main__':
    S = Solution()
    print(S.longestConsecutive([100, 4, 200, 1, 3, 2]))
