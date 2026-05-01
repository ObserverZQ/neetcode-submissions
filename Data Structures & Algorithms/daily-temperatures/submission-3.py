class Solution:
    # idea: use a stack to keep track of temperatures and indices that haven't been covered
    # by warmer temps after them. this way we simply have to compare stack top with the current temperature
    # and only have to iterate the list once compared to brute force.
    # time: O(n), space: O(n)
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []
        for i, val in enumerate(temperatures):
            # print(f'val: {val}, i: {i}')
            while stack and stack[len(stack) - 1][0] < val:
                out = stack.pop()
                # print(f'out: {out}')
                res[out[1]] = i - out[1]
                # print(f'res: {res}')
            stack.append((val, i))
            # print(f'after appended: {stack}')
        return res