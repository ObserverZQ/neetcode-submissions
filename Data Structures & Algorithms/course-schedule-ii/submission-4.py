class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # num of prerequisites for each course
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for crs, pre in prerequisites:
            indegree[crs] += 1
            adj[pre].append(crs)
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        res = []
        finishedCount = 0
        while q:
            crs = q.popleft()
            res.append(crs)
            finishedCount += 1

            for nei in adj[crs]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return res if finishedCount == numCourses else []