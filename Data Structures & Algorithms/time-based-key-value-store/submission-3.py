from sortedcontainers import SortedDict
# same idea, but used external apis and libs.
# SortedDict for defaultdict makes the key in the dict sorted automatically
# timestamps.bisect_right(timestamp) finds the insertion point for a value in a sorted list to maintain sorted order
# so by minusing one we get the rightmost index such that i <= timestamp
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
            closest_time = timestamps.iloc[idx]
            return timestamps[closest_time]
        return ""