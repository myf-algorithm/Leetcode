class Solution(object):
    def sortColors(self, nums):
        """
        初始化0的最右边界：p0 = 0。在整个算法执行过程中 nums[idx < p0] = 0.
        初始化2的最左边界 ：p2 = n - 1。在整个算法执行过程中 nums[idx > p2] = 2.
        初始化当前考虑的元素序号 ：curr = 0.

        While curr <= p2 :
            若 nums[curr] = 0 ：交换第 curr个 和 第p0个 元素，并将指针都向右移。
            若 nums[curr] = 2 ：交换第 curr个和第 p2个元素，并将 p2指针左移 。
            若 nums[curr] = 1 ：将指针curr右移。
        """
        p0 = curr = 0
        p2 = len(nums) - 1
        while curr <= p2:
            if nums[curr] == 0:
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                curr += 1


if __name__ == '__main__':
    S = Solution()
    a = [2, 0, 2, 1, 1, 0]
    S.sortColors(a)
    print(a)
