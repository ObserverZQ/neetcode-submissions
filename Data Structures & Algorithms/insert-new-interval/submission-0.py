class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i, (s, e) in enumerate(intervals):
            # overall smaller than cur interval
            if newInterval[1] < s:
                res.append(newInterval)
                return res + intervals[i:]
           
            # overall bigger than cur interval
            elif newInterval[0] > e:
                res.append([s, e])
            # overlap with cur interval
            else:
                # integrate the cur interval into newInterval
                newInterval = [min(newInterval[0], s), max(newInterval[1], e)]
        res.append(newInterval)
        return res