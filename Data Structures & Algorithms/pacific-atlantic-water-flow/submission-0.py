class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # dfs
        # which cells can water flow FROM each ocean? start from seaside cells to equally high or higher cells. accumulate cells from pacific and atlantic and then return cells that exist in both sets
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()
        
        def dfs(r, c, reachable, prevHeight):
            if (r, c) in reachable or r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if heights[r][c] < prevHeight:
                return
            reachable.add((r, c))

            dfs(r + 1, c, reachable, heights[r][c])
            dfs(r - 1, c, reachable, heights[r][c])
            dfs(r, c + 1, reachable, heights[r][c])
            dfs(r, c - 1, reachable, heights[r][c])

        # pac
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])

        # atl
        for c in range(cols):
            dfs(rows - 1, c, atl, heights[rows - 1][c])
        for r in range(rows):
            dfs(r, cols - 1, atl, heights[r][cols - 1])

        return [[r, c] for r, c in pac if (r, c) in atl]