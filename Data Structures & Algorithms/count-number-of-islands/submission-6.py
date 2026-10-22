class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # use dfs to explore one continued island, mark it as 0 after visiting, return true if it is the last 1?
        # iterate all 1's on the whole grid
        rows, cols = len(grid), len(grid[0])
        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(r: int, c: int):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if grid[r][c] == '0':
                return
            grid[r][c] = '0'
            for dr, dc in neighbors:
                dfs(r+dr, c+dc)
        res = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    dfs(i, j)
                    res += 1
        return res