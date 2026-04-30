class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pars = { ')': '(', '}': '{', ']': '['}

        for c in s:
            # a closing parenthesis, pop an opening parenthesis to check if they match
            if c in pars:
                if not stack or stack.pop() != pars[c]:
                    return False
            # an openning parenthesis, push to stack
            else:
                stack.append(c)
        # make sure all openning parenthesis have been matched
        return len(stack) == 0