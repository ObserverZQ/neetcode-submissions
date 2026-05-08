class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profitMax = 0
        buy = 0
        n = len(prices)
        if n == 1:
            return 0
        for i in range(1, n):
            while prices[buy] > prices[i] and buy < i:
                buy += 1
            if buy == i:
                continue
            # now the buy price is lower than the current price
            profit = prices[i] - prices[buy]
            profitMax = max(profit, profitMax)
        return profitMax