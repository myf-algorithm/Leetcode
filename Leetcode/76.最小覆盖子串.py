class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        from collections import Counter
        mem = Counter(t)
        t_len = len(t)

        minL, minR = 0, float('inf')

        l = 0
        for r, c in enumerate(s):
            if mem[c] > 0:
                t_len -= 1
            mem[c] -= 1

            if t_len == 0:
                while mem[s[l]] < 0:
                    mem[s[l]] += 1
                    l += 1

                if r - l < minR - minL:
                    minL, minR = l, r

                mem[s[l]] += 1
                t_len += 1
                l += 1

        return "" if minR == float('inf') else s[minL:minR + 1]


if __name__ == '__main__':
    S = Solution()
    s = "bbaa"
    t = "aba"
    print(S.minWindow(s, t))
