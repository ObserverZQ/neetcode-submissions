class Solution:
    # Time: O(k * C(n, k)), and the first 'k' is the size of each combination
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        # i: current number, 1 to n
        # curArr: the list accumulated so far
        def helper(i: int, curArr: List[int]) -> None:
            if len(curArr) == k:
                res.append(curArr.copy())
                return
            if i > n:
                return
            
            # notice the upper bound is n + 1 for us to append n in the curArr
            for j in range(i, n + 1):
                curArr.append(j)
                helper(j + 1, curArr)
                curArr.pop()

        helper(1, [])
        return res