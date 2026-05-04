class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        rightMax = arr[n - 1]
        arr[n - 1] = -1
        for i in range(n - 2, -1, -1):
            temp = max(rightMax, arr[i]) # get rightMax including the current element
            arr[i] = rightMax # replace the cur with rightMax excluding the cur
            rightMax = temp
        return arr