class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False
        if sum(nums)%2 == 1:
            return False
        dp = [0 for _ in range(sum(nums)//2+1)]

        dp[0] = 1
        dp[nums[0]] = 1
        for i in range(1,len(nums)):
            #print(nums[i])
            for j in range(len(dp)-1,-1,-1):
    
                    if dp[j] == 1:
                        if j+nums[i] < len(dp):
                            dp[j+nums[i]] = 1
                #print(dp)
        #print(dp)
        if dp[len(dp)-1] == 1:
            return True 
        return False 
            
