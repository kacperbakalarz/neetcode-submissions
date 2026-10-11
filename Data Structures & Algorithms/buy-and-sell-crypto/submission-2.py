class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0 for _ in range(len(prices))]
        dp2 = [0 for _ in range(len(prices))]
        minimal = prices[0]
        for i in range(len(prices)):
            dp[i] = prices[i] - minimal
            minimal = min(minimal,prices[i])
        return max(dp)
