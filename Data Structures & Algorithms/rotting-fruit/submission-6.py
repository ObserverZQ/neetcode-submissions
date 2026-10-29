class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # idea: start from all rotten fruits: 2
        # use a stopwatch and a counter
        # mark all 1 neighbors of 2 to 2 in each round
        # use bfs.
        # first check the number of fresh fruits
        # when done, compare the two numbers
        # return -1 if not match otherwise the stopwatch
        freshCount = 0
        rotten_queue = deque()
        time = 0
        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    freshCount += 1
                elif grid[i][j] == 2:
                    rotten_queue.append((i, j))
        # edge case: no rotten fruit / fresh fruit at all
        if freshCount == 0:
            return 0
        if not rotten_queue:
            return -1
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        while rotten_queue:
            lenq = len(rotten_queue)
            # print('time 1', time)
            # print('rotten_queue 1', rotten_queue)
            # in one minute's lapse
            for _ in range(lenq):
                r, c = rotten_queue.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        rotten_queue.append((nr, nc))
                        freshCount -= 1
                        grid[nr][nc] = 0
            
            if rotten_queue:
                time += 1
            # print('rotten_queue 2', rotten_queue, time)
        return time if freshCount == 0 else -1


        