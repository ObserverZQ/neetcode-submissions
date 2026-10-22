class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # count the dependency for each course
        # start from courses that are not prerequisites .
        # after done, decrease one for those courses that depend on it.
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
        while q:
            node = q.popleft()
            finishCount += 1
            for crs in adj[node]:
                indegree[crs] -= 1
                if indegree[crs] == 0:
                    q.append(crs)
        return finishCount == numCourses