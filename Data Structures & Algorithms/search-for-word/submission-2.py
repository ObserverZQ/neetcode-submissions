class Solution:
    # backtracking + hashset
    # time: O(m * 4 to the nth power), space: O(n)
    # where m is the number of cells in the board and n is the length of the word
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(r, c, i):
            if i == len(word):
                return True

            if r < 0 or r >= rows or c < 0 or c >= cols or word[i] != board[r][c] or (r, c) in visited:
                return False
            
            visited.add((r, c))

            res = (dfs(r+1, c, i+1) or dfs(r-1,c,i+1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1))
            
            visited.remove((r, c))
            return res
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False