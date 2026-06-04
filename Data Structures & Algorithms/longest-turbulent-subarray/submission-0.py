class Solution:
    # sliding window, time: O(n), space: O(1)
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l, r, res = 0, 1, 1
        prev = '' # the comparison sign of the current element and its prev

        while r < len(arr):
            if arr[r - 1] > arr[r] and prev != '>': # prev can be '' or '<'
                res = max(res, r - l + 1)
                r += 1
                prev = '>'
            elif arr[r - 1] < arr[r] and prev != '<':
                res = max(res, r - l + 1)
                r += 1
                prev = '<'
            else:
                r = r + 1 if arr[r] == arr[r - 1] else r
                l = r - 1
                prev = ''
        return res
