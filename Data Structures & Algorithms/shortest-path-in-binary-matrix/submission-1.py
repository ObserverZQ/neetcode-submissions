class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        start = (0, 0)
        n = len(grid)
        goal = (n - 1, n - 1)
        length = 0

        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        visited = set()
        visited.add(start)
        queue = deque()
        queue.append(start)

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == n - 1 and c == n - 1:
                    return length + 1
                # possible adjacent cells
                neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1], [-1, -1], [-1, 1], [1, -1], [1, 1]]
                for dr, dc in neighbors:
                    coord = (r+dr, c+dc)
                    if min(coord) < 0 or max(coord) >= n or coord in visited or grid[r+dr][c+dc] == 1:
                        continue
                    queue.append(coord)
                    visited.add(coord)
            length += 1
        return -1