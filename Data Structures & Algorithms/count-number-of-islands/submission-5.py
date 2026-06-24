class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # make visited grid 0 temporarily
        def dfs(r: int, c: int):
            # base case
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
                return

            # meed a one here
            grid[r][c] = '0'
            for dr, dc in directions:
                dfs(r+dr, c+dc)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(r, c)
                    count += 1
        return count