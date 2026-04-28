class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        seen = []
        for i in range(n):
            for j in range(n):
                val = board[i][j]
                if val != '.':
                    seen += [(i, val), (val, j), (i//3, j//3, val)]
        return len(seen) == len(set(seen))
