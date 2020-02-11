class Solution:
    def romanToInt(self, s: str) -> int:
        table = {'IV': 4,
                 'IX': 9,
                 'XL': 40,
                 'XC': 90,
                 'CD': 400,
                 'CM': 900}
        num = {'I': 1,
               'V': 5,
               'X': 10,
               'L': 50,
               'C': 100,
               'D': 500,
               'M': 1000}
        res = 0
        i = 0
        while i < len(s):
            if (i < len(s) - 1) and (s[i] + s[i + 1]) in table:
                res += table[s[i] + s[i + 1]]
                i += 2
            else:
                res += num[s[i]]
                i += 1
        return res


if __name__ == '__main__':
    S = Solution()
    s = "MCMXCIV"
    print(S.romanToInt(s))
