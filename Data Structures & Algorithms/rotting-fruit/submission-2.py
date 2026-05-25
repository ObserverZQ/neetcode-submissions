class Solution:
    # matrix bfs
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        freshCount = 0
        time = 0
        # get all the 2's in the grid
        # and check edge cases
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                    # visited.add((i, j))
                elif grid[i][j] == 1:
                    freshCount += 1
        if not queue and freshCount > 0:
            return -1
        if freshCount == 0:
            return 0

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while queue:
            freshPrev = freshCount
            for i in range(len(queue)):
                r, c = queue.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # row in range(len(grid)
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        freshCount -= 1
            if not queue and freshCount == 0:
                return time
            elif freshCount == freshPrev:
                return -1
            else:
                time += 1
        return time
        
        