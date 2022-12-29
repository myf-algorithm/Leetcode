def calculate(self, s: str) -> int:
    stack = []
    sign = 1  # 记录符号
    num = 0  # 数字
    res = 0  # 结果
    for c in s:
        if c.isdigit():
            num = num * 10 + int(c)
        elif c == '+':
            res += sign * num
            num = 0
            sign = 1
        elif c == '-':
            res += sign * num
            num = 0
            sign = -1
        elif c == '(':
            stack.append(res)
            stack.append(sign)
            sign = 1
            res = 0
        elif c == ')':
            res += sign * num
            num = 0
            res = stack.pop() * res + stack.pop()
    res += sign * num
    return res
