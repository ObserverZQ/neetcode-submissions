class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(r: int, c: int):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0
            if grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            res = 1
            for dr, dc in neighbors:
                res += dfs(r+dr, c+dc)
            # print('r', r, 'c', c, res)
            return res
        # res = 0
        maxArea = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    # print('i: ', i, 'j: ', j)
                    area = dfs(i, j)
                    maxArea = max(maxArea, area)
        return maxArea