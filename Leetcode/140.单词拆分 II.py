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


class Solution1:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict2Set = set(wordDict)
        import collections
        dic = collections.defaultdict(list)

        def backtracking(s):
            if s in dic:
                return dic[s]
            res = []
            if not s:
                return [[]]
            for i in range(len(s)):
                if s[:i + 1] in wordDict2Set:
                    cur = backtracking(s[i + 1:])
                    for tmp in cur:
                        tmp = [s[:i + 1]] + tmp
                        res.append(tmp)
            dic[s] = res
            return res

        return [' '.join(tmp) for tmp in backtracking(s)]
