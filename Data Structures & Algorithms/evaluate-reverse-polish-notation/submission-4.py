class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def add(a, b):
            return a + b
        def minus(a, b):
            return a - b
        def multiply(a, b):
            return a * b
        def divide(a, b):
            # another more efficient way: stack.append(int(float(b) / a))
            '''
            Step 1 (float(b) / a): Calculates the exact decimal.-6 / 4 -> -1.5
            Step 2 (int(...)): In Python, passing a float to int() truncates it.
            It simply "chops off" everything after the decimal point.int(-1.5) -> -1 int(1.5) -> 1
            '''
            return int(float(a) / b)
            # a, b = int(a), int(b)
            # if a % b == 0:
            #     return a // b
            # notice: division between integers always truncates toward zero.
            # return a // b if (a >= 0 and b > 0) or (a <= 0 and b < 0) else a // b + 1
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
                stack.append(int(t))
        print(f'stack, {stack}')
        return int(stack[0]) # in case no calculation happened
        