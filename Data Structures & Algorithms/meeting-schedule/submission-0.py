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
        new_intervals = sorted(intervals, key = lambda x: x.start)

        for i in range(1, len(new_intervals)):
            prev_end = new_intervals[i - 1].end
            cur_start = new_intervals[i].start
            if cur_start < prev_end:
                return False
        return True