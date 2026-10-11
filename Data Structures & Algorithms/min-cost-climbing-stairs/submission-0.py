class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 2:
            return min(cost[0],cost[1])
        if n == 1:
            return min(cost[0])
        if n == 0:
            return 0 
        dp = [0 for _ in range(n)]
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2,n):
            dp[i] = min(dp[i-1]+cost[i],dp[i-2]+cost[i])
            #print(dp)

        return min(dp[n-1],dp[n-2])
        