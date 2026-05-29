class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = { i: [ ] for i in range(numCourses) }
        for c, pre in prerequisites:
            preMap[c].append(pre)

        visiting = set()

        def dfs(c):
            # we meeta course already met, so it is a dependency cycle
            if c in visiting:
                return False
            # we meet a course that has no prerequisites,
            # so we can start from that course and eventually take numCourses courses
            if preMap[c] == []:
                return True
            
            visiting.add(c)

            for pre in preMap[c]:
                if not dfs(pre):
                    return False
            
            visiting.remove(c)
            preMap[c] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

