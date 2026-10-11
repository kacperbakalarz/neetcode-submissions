class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = float('inf')
        if len(nums) == 1:
            return 0
        for i in range(len(nums)-k+1):
            roznica = nums[i + k - 1] - nums[i]
            #print(roznica,nums[i:i+k])
            ans = min(ans,roznica)
        return ans 

        