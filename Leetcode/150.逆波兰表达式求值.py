class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i in tokens:
            if i in {'+', '-', '*', '/'}:
                a, b = stack.pop(), stack.pop()
                stack.append(str(int(eval(b + i + a))))
            else:
                stack.append(i)
        return stack[-1]


if __name__ == '__main__':
    print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
