class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                tmp = 0
                while i < len(s) and s[i].isdigit():
                    tmp = tmp * 10 + int(s[i])
                    i += 1
                stack.append(tmp)
                # 如果栈中没有乘除，先算出来
                while len(stack) > 1 and stack[-2] in {"*", "/"}:
                    stack.pop()
                    opt = stack.pop()
                    if opt == "*":
                        stack.append(stack.pop() * tmp)
                    else:
                        stack.append(stack.pop() // tmp)
            elif s[i] in {"*", "/", "+", "-"}:
                stack.append(s[i])
                i += 1
            else:
                i += 1
        sign = 1
        res = 0
        for t in stack:
            if t == "+":
                sign = 1
            elif t == "-":
                sign = -1
            else:
                res += (sign * t)
        return res

    def calculate1(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 小trick
        s += "+0"
        stack = []
        num = 0
        # 记录前一个符号
        sign = "+"
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in {"+", "-", "*", "/"}:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack[-1] = stack[-1] * num
                elif sign == "/":
                    # 解决python的负数下取整
                    if stack[-1] < 0:
                        stack[-1] = -(-stack[-1] // num)
                    else:
                        stack[-1] = stack[-1] // num
                sign, num = c, 0
        return sum(stack)

