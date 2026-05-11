class Solution:
    # for iterative solution, we calculate the steps bottom-up.
    # we can think of for every integer, the number of steps to reach it
    # is the number of steps to reach the previous two contingent numbers 
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        a, b = 0, 1
        # for n == 2, we get the first round: a = 1, b = 1
        # the second round: a = 1, b = 2 so we have steps 2 when n is 2.
        for i in range(n):
            a, b = b, a + b
        return b
        