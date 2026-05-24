class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        m = len(image)
        n = len(image[0])
        def dfs(r: int, c: int, visited: object) -> None:
            # check r and c legality
            if r < 0 or c < 0 or r >= m or c >= n or (r, c) in visited:
                return
            # check color
            if image[r][c] != original_color:
                return
            
            image[r][c] = color
            visited.add((r, c))

            dfs(r + 1, c, visited)
            dfs(r - 1, c, visited)
            dfs(r, c + 1, visited)
            dfs(r, c - 1, visited)

            # we may not have to remove (r, c) from visited

        dfs(sr, sc, set())
        return image