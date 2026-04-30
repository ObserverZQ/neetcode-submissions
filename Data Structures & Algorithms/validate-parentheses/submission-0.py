class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pars = { ')': '(', '}': '{', ']': '['}

        for i in range(len(s)):
            # a closing parenthesis, pop an opening parenthesis to check if they match
            if s[i] in pars:
                # print(f'in pars, {s[i]}, {stack}')
                if len(stack) == 0:
                    return False
                sym = stack.pop()
                # print(f'sym, {sym}, {pars[s[i]]}, {pars[s[i]] == sym}')
                if sym != pars[s[i]]:
                    return False
            # an openning parenthesis, push to stack
            else:
                stack.append(s[i])
                # print(f'stack, {stack}')
        # make sure all openning parenthesis have been matched
        return len(stack) == 0