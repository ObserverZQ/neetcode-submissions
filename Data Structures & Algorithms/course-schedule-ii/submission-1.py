class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)
        for c, pre in prerequisites:
            adj[c].append(pre)
        print(f'adj: {adj}')

        res = []
        path = set()
        visited = set()

        def dfs(c: int):
            print(f'dfs: {c}')
            if c in path:
                return False
            if c in visited:
                return True
            visited.add(c)
            path.add(c)
            for pre in adj[c]:
                print(f'pre: {pre}')
                if not dfs(pre):
                    return False
            # path.remove(c)
            res.append(c)
            path.remove(c)
            return True
        for c in range(numCourses):
            if not dfs(c):
                return []
        return res