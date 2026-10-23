class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def bfs(r: int, c: int):
            q = deque([(r, c)])
            grid[r][c] = 0
            res = 1
            while q:
                qr, qc = q.popleft()
                
                for dr, dc in neighbors:
                    nr, nc = qr+dr, qc+dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        res += 1
                        q.append((nr, nc))
                        grid[nr][nc] = 0
            return res
        maxArea = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    area = bfs(i, j)
                    maxArea = max(maxArea, area)
        return maxArea