class Solution:
    # for recursion solution,
    # we use a set to record calculated steps for smaller n to accelerate
    def climbStairs(self, n: int) -> int:
        stepMap = {}
        def steps(n: int) -> int:
            if n<= 1:
                return 1
            elif n in stepMap:
                return stepMap[n]
            else:
                stepMap[n] = steps(n - 1) + steps(n - 2)
                return stepMap[n]
        return steps(n)