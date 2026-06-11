class Solution:
    # bfs. once we find an island grid we use deque to explore neighbors until the current island is finished exploring.
    # time: O(m * n), space: O(m * n)
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def bfs(r, c):
            queue = deque([(r,c)])

            while queue:
                r, c = queue.popleft()
                grid[r][c] = '0'
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                        queue.append((r+dr, c+dc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    bfs(r, c)
                    islands += 1
        return islands