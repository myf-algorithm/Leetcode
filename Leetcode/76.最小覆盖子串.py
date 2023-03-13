class Solution(object):
    def minWindow(self, s, t):
        from collections import defaultdict
        findout = defaultdict(int)
        for i in t:
            findout[i] += 1
        min_len, res = float('inf'), ""
        l, counter = len(s), len(t)
        left = right = 0
        while right < l:
            if findout[s[right]] > 0:
                counter -= 1
            findout[s[right]] -= 1
            right += 1
            while counter == 0:
                if min_len > right - left:
                    min_len = right - left
                    res = s[left:right]
                if findout[s[left]] == 0:
                    counter += 1
                findout[s[left]] += 1
                left += 1
        return res


if __name__ == '__main__':
    S = Solution()
    s = "bbaa"
    t = "aba"
    print(S.minWindow(s, t))
