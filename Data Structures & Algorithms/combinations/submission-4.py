class Solution:
    # Time: O(k * 2^n), and the first 'k' is the size of each combination
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
            curArr.append(i)
            helper(i + 1, curArr)
            curArr.pop()
            helper(i + 1, curArr)

        helper(1, [])
        return res