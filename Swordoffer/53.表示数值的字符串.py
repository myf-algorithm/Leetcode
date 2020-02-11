# -*- coding:utf-8 -*-
# 请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
# 例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。
# 但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。


class Solution:
    def isNumeric(self, s):
        isAllowDot = True
        isAllowE = True
        for i in range(len(s)):
            if s[i] in "+-" and (i == 0 or s[i - 1] in "eE") and i < len(s) - 1:
                continue
            elif isAllowDot and s[i] == ".":
                isAllowDot = False
                if i >= len(s) - 1 or s[i + 1] not in "0123456789":
                    return False
            elif isAllowE and s[i] in "Ee":
                isAllowDot = False
                isAllowE = False
                if i >= len(s) - 1 or s[i + 1] not in "0123456789+-":
                    return False
            elif s[i] not in "0123456789":
                return False
        return True


class Solution1:
    # s字符串
    def isNumeric(self, s):
        INVALID = 0
        SPACE = 1
        SIGN = 2
        DIGIT = 3
        DOT = 4
        EXPONENT = 5
        # 0invalid, 1space, 2sign, 3digit, 4dot, 5exponent, 6num_inputs
        transitionTable = [[-1, 0, 3, 1, 2, -1],  # 0 no input or just spaces
                           [-1, 8, -1, 1, 4, 5],  # 1 input is digits
                           [-1, -1, -1, 4, -1, -1],  # 2 no digits in front just Dot
                           [-1, -1, -1, 1, 2, -1],  # 3 sign
                           [-1, 8, -1, 4, -1, 5],  # 4 digits and dot in front
                           [-1, -1, 6, 7, -1, -1],  # 5 input 'e' or 'E'
                           [-1, -1, -1, 7, -1, -1],  # 6 after 'e' input sign
                           [-1, 8, -1, 7, -1, -1],  # 7 after 'e' input digits
                           [-1, 8, -1, -1, -1, -1]]  # 8 after valid input input space
        state = 0
        i = 0
        while i < len(s):
            inputtype = INVALID
            if s[i] == ' ':
                inputtype = SPACE
            elif s[i] == '-' or s[i] == '+':
                inputtype = SIGN
            elif s[i] in '0123456789':
                inputtype = DIGIT
            elif s[i] == '.':
                inputtype = DOT
            elif s[i] == 'e' or s[i] == 'E':
                inputtype = EXPONENT
            state = transitionTable[state][inputtype]
            if state == -1:
                return False
            else:
                i += 1
        return state == 1 or state == 4 or state == 7 or state == 8


if __name__ == '__main__':
    S = Solution()
    print(S.isNumeric('-1234'))
