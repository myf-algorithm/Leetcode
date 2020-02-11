import math


class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        elif x > 0:
            res = str(x)[::-1]
            while res[0] == '0':
                res = res[1:]
            return int(res) if (math.pow(2, 31) * -1) <= int(res) <= (math.pow(2, 31) - 1) else 0
        else:
            res = str(x)[1:][::-1]
            while res[0] == '0':
                res = res[1:]
            return int(res) * -1 if (math.pow(2, 31) * -1) <= (int(res) * -1) <= (math.pow(2, 31) - 1) else 0


if __name__ == '__main__':
    s = Solution()
    print(s.reverse(1534236469))
