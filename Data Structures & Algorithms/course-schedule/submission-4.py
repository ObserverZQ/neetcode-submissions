class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # dfs. time: O(V+E), space: O(V+E)
        # build ajacency list for course 0 - (numcourses - 1)
        preMap = { i: [] for i in range(numCourses)}
        for c, p in prerequisites:
            preMap[c].append(p)
        
        visited = set()

        # if we can finish the course
        def dfs(crs):
            if crs in visited:
                # found a cycle in the prerequisite chain, we can never finish a course
                return False
            # found a course with no prerequisites, so we can for sure finish it!
            if preMap[crs] == []:
                return True
            
            # the course has prerequisites, so we see if every one of them can be finished (or their prerequisites can be finished, with recursion)
            # add the current course to the path we are exploring
            visited.add(crs)
            for p in preMap[crs]:
                if not dfs(p):
                    return False
            # we have explored its prerequisites,
            # so we can remove it in the set to call it a day
            visited.remove(crs)
            preMap[crs] = []
            # all the prerequisites can be finished
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True