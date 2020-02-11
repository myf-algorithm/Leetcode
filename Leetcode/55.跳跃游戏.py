class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        贪心算法
        """
        # 当前位置的下标
        start = 0
        # 从当前位置到达的最远位置
        end = 0
        # 数组的长度
        n = len(nums)
        while start <= end and end < len(nums) - 1:
            # 尝试去找最大的位置
            end = max(end, nums[start] + start)
            start += 1
        return end >= n - 1


if __name__ == '__main__':
    S = Solution()
    print(S.canJump([2, 3, 1, 1, 4]))
