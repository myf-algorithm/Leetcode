class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        wordDict2Set = set(wordDict)

        def backtracking(s, path):
            if not s:
                res.append(' '.join(path))
                return
            for i in range(len(s)):
                if s[:i + 1] in wordDict2Set:
                    path.append(s[:i + 1])
                    backtracking(s[i + 1:], path)
                    path.pop()

        backtracking(s, [])
        return res
