"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 1:
            return True
        # sorted returns a new array. we can use list.sort() alternatively.
        # intervals = sorted(intervals, key = lambda x: x.start)
        intervals.sort(key = lambda x: x.start)
        for i in range(1, len(intervals)):
            prev_end = intervals[i - 1].end
            cur_start = intervals[i].start
            if cur_start < prev_end:
                return False
        return True