class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        goal = (n - 1, n - 1)

        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        visited = set((0, 0))
        queue = deque([(0, 0, 1)]) # r, c, length including the current cell

        while queue:
            for i in range(len(queue)):
                r, c, length = queue.popleft()
                if r == n - 1 and c == n - 1:
                    return length
                # possible adjacent cells
                neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1], [-1, -1], [-1, 1], [1, -1], [1, 1]]
                for dr, dc in neighbors:
                    nr, nc = r+dr, c+dc
                    if (0 <= nr < n) and (0 <= nc < n) and (nr, nc) not in visited and grid[nr][nc] == 0:
                        queue.append((nr, nc, length + 1))
                        visited.add((nr, nc))
        return -1