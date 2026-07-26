class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        path = [] # detect cycle
        visited = set() # detect visited
        adj = {}
        def dfs(src):
            if src in path:
                return False
            if src in visited:
                return True

            path.append(src)
            for nei in adj[src]:
                if not dfs(nei):
                    return False
            path.remove(src)
            visited.add(src)
            return True
        
        # topological sort
        # 1. create adjacent list
        for n in range(numCourses):
            adj[n] = []
        for c, pre in prerequisites:
            adj[c].append(pre)
        
        for n in range(numCourses):
            if not dfs(n):
                return False
        return True