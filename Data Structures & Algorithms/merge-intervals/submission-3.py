class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # if the cur interval's lower bound is smaller than the prev's upper bound, we can merge them. otherwise we start a new interval storage
        intervals.sort()
        res = []
        n = len(intervals)
        cur = intervals[0]
        for i in range(1, n):
            # overlap and need to expand
            if cur[1] >= intervals[i][0] and cur[1] < intervals[i][1]:
                cur[1] = intervals[i][1]
            # disconnected, and overall greater than cur
            elif cur[1] < intervals[i][0]:
                res.append(cur)
                cur = intervals[i]
        res.append(cur)
        return res