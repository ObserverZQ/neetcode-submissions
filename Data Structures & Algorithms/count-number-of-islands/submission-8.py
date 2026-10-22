class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # trap: mark visited immediatly after adding it to the queue, otherwise the same cell gets added to the queue infinitely because it's never marked as visited
        def bfs(r, c):
            q = deque([(r, c)])
            grid[r][c] = '0'
            while len(q):
                qr, qc = q.popleft()
                for dr, dc in neighbors:
                    nr, nc = qr+dr, qc+dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                        q.append((nr, nc))
                        grid[nr][nc] = '0'
        res = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    bfs(i, j)
                    res += 1
        return res