class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for crs, pre in prerequisites:
            indegree[crs] += 1
            adj[pre].append(crs)
        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)
        finishCount = 0
        res = []
        while q:
            node = q.popleft()
            res.append(node)
            finishCount += 1
            for crs in adj[node]:
                indegree[crs] -= 1
                if indegree[crs] == 0:
                    q.append(crs)
        return res if finishCount == numCourses else []