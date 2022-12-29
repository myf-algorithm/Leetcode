class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [int(expression)]
        nums = []
        for i, char in enumerate(expression):
            if char in ['+', '-', '*']:
                # 分解：遇到运算符，计算左右两侧的结果集
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])

                # 合并：根据运算符合并子集的解
                for l in left:
                    for r in right:
                        if char == '+':
                            nums.append(l + r)
                        if char == '-':
                            nums.append(l - r)
                        if char == '*':
                            nums.append(l * r)
        return nums