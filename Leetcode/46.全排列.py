class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        回溯法
        """
        res = []

        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
                return
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i + 1:], tmp + [nums[i]])

        backtrack(nums, [])
        return res

    def permute1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        插入法
        """
        if len(nums) < 2:  # 如果为1个或两个元素直接返回
            return [nums]
        # 逐个元素的插入法，每次插入新元素到所有旧排列的所有能插入的位置生成新排列
        preres = [[nums[0]]]
        for i in nums[1:]:
            res = []
            for temp in preres:
                for j in range(len(temp) + 1):
                    res.append(temp[:j] + [i] + temp[j:])
            preres = res  # 成为旧排列
        return preres


if __name__ == '__main__':
    S = Solution()
    print(S.permute1([1, 2, 3]))

# 回溯法详解：https://www.nowcoder.com/practice/4bcf3081067a4d028f95acee3ddcd2b1?tpId=117&&tqId=34964&rp=1&ru=/ta/job-code-high&qru=/ta/job-code-high/question-ranking
# 回溯法、深度优先搜索（DFS）、动态规划、递归之间的区别
