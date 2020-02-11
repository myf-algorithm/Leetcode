from typing import List


class Solution:
    m = {
        '2': 'abc', '3': 'def', '4': 'ghi',
        '5': 'jkl', '6': 'mno', '7': 'pqrs',
        '8': 'tuv', '9': 'wxyz'
    }

    def dfs(self, i, digits, ans, tmp):
        if i == len(digits):
            ans.append(''.join(tmp))
            return
        for ch in self.m[digits[i]]:
            tmp.append(ch)
            self.dfs(i + 1, digits, ans, tmp)
            tmp.pop()

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        ans = []
        tmp = []
        self.dfs(0, digits, ans, tmp)
        return ans


if __name__ == '__main__':
    S = Solution()
    nums = "23"
    print(S.letterCombinations(nums))
