class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        rows, cols = len(grid), len(grid[0])
        neighbors = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0
            if grid[r][c] == 0:
                return 0
            # an island. start counting neighbors
            grid[r][c] = 0
            area = 1
            for dr, dc in neighbors:
                nr, nc = r + dr, c + dc
                area += dfs(nr, nc)
            return area

        for i in range(rows):
            for j in range(cols):
                area = dfs(i, j)
                if area > maxArea:
                    maxArea = area
        return maxArea