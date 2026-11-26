class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0 # iterate popped
        for push in pushed:
            stack.append(push)
            while i < len(popped) and stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        return len(stack) == 0
            
