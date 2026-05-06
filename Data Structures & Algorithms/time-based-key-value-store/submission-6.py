from sortedcontainers import SortedDict
# same idea, but used external apis and libs.
# Using defaultdict(SortedDict) creates a two-level nested dictionary where any new, top-level key automatically initializes a SortedDict as its value.
# so inside every key we have a sorteddict, every time we set a new timestamp-value for that key it is sorted by timestamp.
# timestamps.bisect_right(timestamp) finds the insertion point for a value in a sorted list to maintain sorted order
# so by minusing one we get the rightmost index such that i <= timestamp
# SortedDict.keys gives us sorted keys from an object
# time O(logn) for set() and O(logn) for get. space O(m*n)
class TimeMap:
    def __init__(self):
        self.m = defaultdict(SortedDict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.m:
            return ""

        timestamps = self.m[key]
        idx = timestamps.bisect_right(timestamp) - 1

        if idx >= 0:
            closest_time = SortedDict.keys(self.m[key])[idx]
            return timestamps[closest_time]
        return ""