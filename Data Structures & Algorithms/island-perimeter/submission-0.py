class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        def check(r, c) -> int:
            if r < 0 or r >= ROW or c < 0 or c >= COL:
                return 1
            if grid[r][c] == 0:
                return 1
            return 0
        res = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] != 1:
                    continue
                neighbors = [(r+1, c), (r-1, c), (r,c+1), (r, c-1)]
                for rn, cn in neighbors:
                    res += check(rn, cn)
        return res
