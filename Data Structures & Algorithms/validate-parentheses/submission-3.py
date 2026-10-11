class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')': '(', '}': '{', ']': '['}
        stack = []
        for c in s:
            # is a closing bracket, check if it can match the last element, e.t. the last left bracket in the stack
            if c in mapping:
                if len(stack) == 0:
                    return False
                start = stack.pop()
                if mapping[c] != start:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0 # check if there are left bracket remaining