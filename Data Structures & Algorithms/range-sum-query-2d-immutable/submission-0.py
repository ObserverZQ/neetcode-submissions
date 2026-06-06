class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        self.prefix = []
        for i in range(m):
            prefix_i = []
            total = 0
            for j in range(n):
                total += sum([matrix[k][j] for k in range(i + 1)])
                prefix_i.append(total)
            self.prefix.append(prefix_i)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        prefixTopLeft = self.prefix[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0
        prefixBottomRight = self.prefix[row2][col2]
        prefixTop = self.prefix[row1 - 1][col2] if row1 > 0 else 0
        prefixLeft = self.prefix[row2][col1 - 1] if col1 > 0 else 0
        res = prefixBottomRight - prefixTop - prefixLeft + prefixTopLeft
        return res

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)