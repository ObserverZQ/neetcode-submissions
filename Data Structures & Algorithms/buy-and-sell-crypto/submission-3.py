class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # problem: when do we slide the front pointer, and what about the latter pointer?
        if len(prices) < 2:
            return 0
        globalMin = prices[0]
        maxP = 0
       
        for p in prices[1:]:
            profit = p - globalMin
            maxP = max(maxP, profit)
            globalMin = min(p, globalMin)
        return maxP
        
        