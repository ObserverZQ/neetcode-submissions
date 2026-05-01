class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def add(a, b):
            return int(a) + int(b)
        def minus(a, b):
            return int(a) - int(b)
        def multiply(a, b):
            return int(a) * int(b)
        def divide(a, b):
            a, b = int(a), int(b)
            if a % b == 0:
                return a // b
            # notice: division between integers always truncates toward zero.
            return a // b if (a >= 0 and b > 0) or (a <= 0 and b < 0) else a // b + 1
        stack = []
        operators = {
            '+': add,
            '-': minus,
            '*': multiply,
            '/': divide
        }
        for t in tokens:
            if t in operators:
                op2 = stack.pop()
                op1 = stack.pop()
                res = operators[t](op1, op2)
                stack.append(res)
            else:
                stack.append(t)
        print(f'stack, {stack}')
        return int(stack[0]) # in case no calculation happened
        