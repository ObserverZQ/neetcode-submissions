class TimeMap:

    def __init__(self):
        self.data = {}
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        # if not self.data.get(key):
        #     self.data[key] = [''] * timestamp
        # elif len(self.data[key]) < timestamp:
        #     self.data[key] += [''] * (timestamp - len(self.data[key]))
        # self.data[key][timestamp - 1] = value
        if not self.data.get(key):
            self.data[key] = [(timestamp, value)]
        else:
            self.data[key].append((timestamp, value))
            self.data[key].sort(key=lambda x: x[0])
        print(f'set, {self.data}')

    def get(self, key: str, timestamp: int) -> str:
        # use binary search to find the timestep closest to the given timestamp
        arr = self.data.get(key)
        if not arr:
            return ''
        l, r = 0, len(arr) - 1
        i = 0
        # m = 1, k = 2, 
        while l <= r:
            m = l + (r - l) // 2
            if arr[m][0] == timestamp:
                return arr[m][1]
            elif arr[m][0] < timestamp:
                i = m
                l = m + 1
            else:
                r = m - 1
        return arr[i][1] if arr[i][0] < timestamp else ''