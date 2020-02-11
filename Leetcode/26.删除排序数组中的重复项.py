from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        temp = nums[0]
        for n in nums[1:]:
            if n == temp:
                nums.remove(temp)
            temp = n
        return len(nums)

    def removeDuplicates1(self, nums: List[int]) -> int:
        pre, cur = 0, 1
        while cur < len(nums):
            if nums[pre] == nums[cur]:
                nums.pop(cur)
            else:
                pre, cur = pre + 1, cur + 1
        return len(nums)


if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
