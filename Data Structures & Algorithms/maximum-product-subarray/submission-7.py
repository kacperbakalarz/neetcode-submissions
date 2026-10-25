class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [-1 for _ in range(len(nums))]
        dp[0] = sorted((nums[0],nums[0]))
        for i in range(1,len(nums)):
            dp[i] = (min(dp[i-1][0]*nums[i],dp[i-1][1]*nums[i],nums[i]),max(dp[i-1][0]*nums[i],dp[i-1][1]*nums[i],nums[i]))
        #print(dp)
        maxi = -float('inf')
        for each in dp:  
            maxi = max(maxi,each[0],each[1])  
        return maxi