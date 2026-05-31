class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        prevRow = [0] * n
        
        for i in range(m - 1, -1, -1):
            curRow = [0] * n
            if obstacleGrid[i][n - 1] == 1:
                curRow[n - 1] = 0
            elif i == m - 1:
                curRow[n - 1] = 1
            else:
                curRow[n - 1] = prevRow[n - 1]
            for j in range(n - 2, -1, -1):
                if obstacleGrid[i][j] == 1:
                    continue
                curRow[j] += curRow[j+1]
                curRow[j] += prevRow[j]
            prevRow = curRow
        return curRow[0]