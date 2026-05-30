class Solution:
    # bottom-up solution. dp.
    def uniquePaths(self, m: int, n: int) -> int:
        prevRow = [0] * n

        for i in range(m - 1, -1, -1):
            curRow = [0] * n
            curRow[n - 1] = 1 # we know that at the last column there is only 1 way(down) to go to the target
            for j in range(n - 2, -1, -1):
                curRow[j] = curRow[j + 1] + prevRow[j]
            prevRow = curRow
        return curRow[0]