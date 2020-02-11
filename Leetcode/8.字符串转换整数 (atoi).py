import math


class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.lstrip()
        if len(str) == 0:
            return 0
        last = 0
        i = 2 if str[0] == '-' or str[0] == '+' else 1
        while i <= len(str):
            try:
                last = int(str[:i])
                i += 1
            except:
                break
        if last < -2147483648:
            return -2147483648
        if last > 2147483647:
            return 2147483647
        return last


if __name__ == '__main__':
    s = Solution()
    print(s.myAtoi("42"))