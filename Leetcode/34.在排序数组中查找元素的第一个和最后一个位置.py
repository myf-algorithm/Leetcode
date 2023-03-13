class Solution(object):
    def searchRange(self, nums, target):
        # 取起始下标
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        # 没找到
        if not nums or nums[l] != target:
            return [-1, -1]
        # 取结果下标
        a, b = l, len(nums) - 1
        while a < b:
            mid = (a + b + 1) // 2
            if nums[mid] <= target:
                a = mid
            else:
                b = mid - 1
        return [l, b]


if __name__ == '__main__':
    S = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 8
    print(S.searchRange(nums, target))
