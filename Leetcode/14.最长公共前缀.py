from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        if len(strs) == 0:
            return res
        elif len(strs) == 1:
            return strs[0]
        min_len = len(strs[0])
        for s in strs[1:]:
            if len(s) < min_len:
                min_len = len(s)
        if min_len == 0:
            return ''
        for i in range(min_len):
            cur = strs[0][i]
            for s in strs[1:]:
                if s[i] != cur:
                    return res
            res += cur
        return res

    def longestCommonPrefix_easy(self, strs: List[str]) -> str:
        s = ""
        for i in zip(*strs):
            if len(set(i)) == 1:
                s += i[0]
            else:
                break
        return s


if __name__ == '__main__':
    S = Solution()
    s = ["flower", "flow", "flight"]
    print(S.longestCommonPrefix_easy(s))
