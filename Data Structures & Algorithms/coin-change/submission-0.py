class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0
        for i in range(amount):
            for j in range(len(coins)):
                if coins[j] + i <= amount:
                    dp[coins[j]+i] = min(dp[coins[j]+i],1 + dp[i])
        if dp[amount] == float("inf"):
            return -1
        return dp[amount]