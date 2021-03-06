class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_table = {}
        for i in nums:
            try:
                hash_table.pop(i)
            except:
                hash_table[i] = 1
        return hash_table.popitem()[0]

    def singleNumber_math(self, nums):
        return 2 * sum(set(nums)) - sum(nums)


if __name__ == '__main__':
    S = Solution()
    a = [2, 2, 1]
    print(S.singleNumber_math(a))
