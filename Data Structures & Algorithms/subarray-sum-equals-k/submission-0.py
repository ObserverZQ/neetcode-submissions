class Solution:
    # key idea: find i and j pairs where prefixSum[j] - prefixSum[i] = k
    # so prefixSum[j] - k = prefixSum[i]
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = curSum = 0
        prefixSums = { 0 : 1 } # record the count of prefixSums. key: sum, value: count
        for num in nums:
            curSum += num
            diff = curSum - k

            res += prefixSums.get(diff, 0)
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0) 
        
        return res