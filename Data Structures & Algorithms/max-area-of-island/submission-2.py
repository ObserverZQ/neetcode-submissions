class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        rows, cols = len(grid), len(grid[0])
        neighbors = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        def bfs(r, c):
            queue = deque([(r, c)])
            area = 0
            while queue:
                r1, c1 = queue.popleft()
                area += 1
                for dr, dc in neighbors:
                    r2, c2 = r1 + dr, c1 + dc
                    if 0 <= r2 < rows and 0 <= c2 < cols and grid[r2][c2] == 1:
                        queue.append((r2, c2))
                        grid[r2][c2] = 0
            return area

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    area = bfs(i, j)
                    if area > maxArea:
                        maxArea = area
        return maxArea