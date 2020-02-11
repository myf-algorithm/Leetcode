class Solution(object):
    def search(self, nums, target):
        # 判断target值是在[左边界, 中值]区间，还是[中值, 右边界]区间
        left, right = 0, len(nums) - 1
        mid = (left + right) // 2

        while left <= right:
            if nums[mid] == target:
                return mid
            judge1 = (nums[left] < nums[mid]) and (target < nums[mid]) and (target >= nums[left])  # 左半边有序
            judge2 = (nums[left] > nums[mid]) and ((target < nums[mid]) or (target >= nums[left]))  # 左半边旋转

            if judge1 or judge2:
                right = mid - 1
                mid = (left + right) // 2
            else:
                left = mid + 1
                mid = (left + right) // 2
        return -1


if __name__ == '__main__':
    S = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    print(S.search(nums, target))
